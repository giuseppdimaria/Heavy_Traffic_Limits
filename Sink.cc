//
// This file is part of an OMNeT++/OMNEST simulation example.
//
// Copyright (C) 2006-2015 OpenSim Ltd.
//
// This file is distributed WITHOUT ANY WARRANTY. See the file
// `license' for details on this and other legal matters.
//

#include "Sink.h"
#include "Job.h"

namespace queueing {

Define_Module(Sink);

void Sink::initialize()
{
    lifeTimeSignal = registerSignal("lifeTime");
    responseTimeSignal = registerSignal("responseTime");      // Registrazione del segnale per il tempo di risposta del Sistema
    keepJobs = par("keepJobs");
}

void Sink::handleMessage(cMessage *msg)
{
    Job *job = check_and_cast<Job *>(msg);
    simtime_t responseTime = simTime() - job->getCreationTime();

    // gather statistics
    emit(responseTimeSignal, responseTime);  // Emit del segnale per il tempo di risposta
    emit(lifeTimeSignal, simTime() - job->getCreationTime());


    if (!keepJobs)
        delete msg;
}

void Sink::finish()
{
}

}; //namespace

