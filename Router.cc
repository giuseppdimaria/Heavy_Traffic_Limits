/*
 * Router.cc
 *
 *  Created on: 31 mag 2023
 *      Author: giuse
 */



#include <omnetpp.h>

using namespace omnetpp;


namespace queueing {

class Router : public cSimpleModule
{
  private:
    double switchProbability;

  protected:
    virtual void initialize() override;
    virtual void handleMessage(cMessage *msg) override;
};

Define_Module(Router);

void Router::initialize()
{
    switchProbability = par("switchProbability").doubleValue();
}

void Router::handleMessage(cMessage *msg)
{
    // Se il valore casuale  minore della probabilit di cambio, il messaggio viene inviato a Server2
    if (uniform(0, 1) < switchProbability) {
        EV << "Job inviato a Server2." << endl;
        send(msg, "out", 0);
    }
    // Altrimenti, se il valore casuale  minore di 0.5, il messaggio viene inviato a Server3
    else {
        EV << "Job inviato a Server3." << endl;
        send(msg, "out", 1);
    }
}

}
