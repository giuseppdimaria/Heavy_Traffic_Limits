//
// This file is part of an OMNeT++/OMNEST simulation example.
//
// Copyright (C) 2006-2015 OpenSim Ltd.
//
// This file is distributed WITHOUT ANY WARRANTY. See the file
// `license' for details on this and other legal matters.
//

#include "Server.h"
#include "Job.h"
#include "SelectionStrategies.h"
#include "IPassiveQueue.h"

namespace queueing {

Define_Module(Server);

Server::Server()
{
    selectionStrategy = nullptr;    // puntatore a strategia di selezione
    jobServiced = nullptr;          // job in servizio
    endServiceMsg = nullptr;        // job di fine servizio
    allocated = false;
}

Server::~Server()
{
    delete selectionStrategy;
    delete jobServiced;
    cancelAndDelete(endServiceMsg);
}

void Server::initialize()
{
    busySignal = registerSignal("busy");
    emit(busySignal, false);

    endServiceMsg = new cMessage("end-service");    // creo messaggio di fine servizio
    jobServiced = nullptr;      // job in servizio
    allocated = false;

    responseTimeSignal = registerSignal("responseTime");

    // creo strategia di selezione
    selectionStrategy = SelectionStrategy::create(par("fetchingAlgorithm"), this, true);
    // controllo se la strategia di selezione esiste
    if (!selectionStrategy)
        throw cRuntimeError("invalid selection strategy");
    // registra e emetti segnale "droppedForDeadline"
    droppedForDeadlineSignal = registerSignal("droppedForDeadline");
    checkJobDeadline = par("checkJobDeadline").boolValue();
}

void Server::handleMessage(cMessage *msg)
{
    // se il messaggio ricevuto è quello di fine servizio
    if (msg == endServiceMsg) {
        ASSERT(jobServiced != nullptr); // controlla se job in servizio non è nullo
        ASSERT(allocated);              // controlla se 'allocated' è true
        simtime_t d = simTime() - endServiceMsg->getSendingTime();      // calcola durata del servizio 'serviceTime'
        jobServiced->setTotalServiceTime(jobServiced->getTotalServiceTime() + d);
        send(jobServiced, "out");

        jobServiced = nullptr;  // Reset del puntatore al job in servizio
        allocated = false;
        emit(busySignal, false);    // emetti segnale 'busy' come false

        emit(responseTimeSignal, d);


        int k = selectionStrategy->select();            // Esame di tutte le code di input e richiesta di un nuovo job da una coda non vuota
        if (k >= 0) {                                   // Se è stata selezionata una coda valida
            EV << "requesting job from queue " << k << endl;
            cGate *gate = selectionStrategy->selectableGate(k);
            check_and_cast<IPassiveQueue *>(gate->getOwnerModule())->request(gate->getIndex());     // richiesta di un job alla coda
        }
    }
    else {
        // Se il messaggio ricevuto non è il messaggio di fine servizio
        if (!allocated)
            error("job arrived, but the sender did not call allocate() previously");
        if (jobServiced)    // se un job è già in servizio
            throw cRuntimeError("a new job arrived while already servicing one");
        jobServiced = check_and_cast<Job *>(msg);   // cast del messaggio ricevuto a 'Job'
        simtime_t serviceTime = par("serviceTime"); // ottengo 'serviceTime'


        // se la Deadline del job è scaduta, allora fa il drop del job
        if (checkJobDeadline) {
            if (jobServiced->getAbsoluteDeadline() < simTime()) {
                EV << "Dropped!" << endl;
                if (hasGUI())
                    bubble("Dropped!");
                emit(droppedForDeadlineSignal, 1);      // Emittente del segnale "droppedForDeadline" con valore 1

                delete msg;                             // dealloca messaggio

                allocated = false;
                jobServiced = nullptr;
                int k = selectionStrategy->select();
                if (k >= 0) {
                    EV << "requesting job from queue " << k << endl;
                    cGate *gate = selectionStrategy->selectableGate(k);
                    check_and_cast<IPassiveQueue *>(gate->getOwnerModule())->request(gate->getIndex());
                }
            }
            else {
                scheduleAt(simTime()+serviceTime, endServiceMsg);   // schedula l'invio del messaggio di fine servizio
                emit(busySignal, true);                             // Emittente del segnale "busy" con valore true
            }
        }
        else {
            scheduleAt(simTime()+serviceTime, endServiceMsg);
            emit(busySignal, true);
        }
    }
}

// Aggiornamento della rappresentazione grafica del modulo
void Server::refreshDisplay() const
{
    getDisplayString().setTagArg("i2", 0, jobServiced ? "status/execute" : "");
}

void Server::finish()
{
}

bool Server::isIdle()
{
    return !allocated;  // we are idle if nobody has allocated us for processing
}

void Server::allocate()
{
    allocated = true;
}

}; //namespace

