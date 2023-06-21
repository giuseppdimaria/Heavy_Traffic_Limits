/*
 * Source.cc
 *
 *  Created on: 31 mag 2023
 *      Author: giuse
 */



#include "Source.h"
#include "Job.h"

namespace queueing {

void SourceBase::initialize()
{
    createdSignal = registerSignal("created");      // registra il segnale 'created' per tenere traccia del numero di job creati
    jobCounter = 0;                                 // variabile per mantenere il conteggio dei job creati
    WATCH(jobCounter);
    jobName = par("jobName").stringValue();
    if (jobName == "")
        jobName = getName();
}

Job *SourceBase::createJob()
{
    char buf[80];
    sprintf(buf, "%.60s-%d", jobName.c_str(), ++jobCounter);
    Job *job = new Job(buf);
    return job;
}

void SourceBase::finish()
{
    emit(createdSignal, jobCounter);
}

//----

Define_Module(Source);


void Source::initialize()
{
    SourceBase::initialize();
    startTime = par("startTime");
    stopTime = par("stopTime");
    numJobs = par("numJobs");
    lambda = par("lambda");

// schedulato il primo messaggio di timer per il tempo di inizio.
    scheduleAt(startTime, new cMessage("newJobTimer"));
}

void Source::handleMessage(cMessage *msg)
{
    ASSERT(msg->isSelfMessage());

    if ((numJobs < 0 || numJobs > jobCounter) && (stopTime < 0 || stopTime > simTime())) {
        // rischedula il tempo per i prossimi job
        scheduleAt(simTime() + exponential(1/lambda), msg);

        Job *job = createJob();
        send(job, "out");
    }
    else {
        // finished
        delete msg;
    }
}



}
