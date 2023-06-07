//
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU Lesser General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
// 
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU Lesser General Public License for more details.
// 
// You should have received a copy of the GNU Lesser General Public License
// along with this program.  If not, see http://www.gnu.org/licenses/.
// 

package org.omnetpp.queueing;

//
// A queue with a built-in server
//
simple PassiveQueue
{
	parameters:
	    @group(Queueing);
        @display("i=block/queue;q=queue");
        
        //@signal[busy](type="bool");
        //@statistic[busy](title="server busy state";record=vector?,timeavg;interpolationmode=sample-hold);
        
        @signal[dropped](type="long");
        @statistic[dropped](title="drop event";record=vector?,count;interpolationmode=none);
        
        @signal[queueLength](type="long");
        @statistic[queueLength](title="queue length";record=vector,timeavg,max;interpolationmode=sample-hold);
        
        @signal[queueingTime](type="simtime_t");
        @statistic[queueingTime](title="queueing time at dequeue";record=vector?,mean,max,histogram;unit=s;interpolationmode=none);
        
        int capacity = default(-1); // capacità illimitata
        bool fifo = default(true);
        string sendingAlgorithm @enum("priority","random","roundRobin","minDelay") = default("priority");
                                     // how the queue tries to find a suitable server for an incoming job
    gates:
        input in[];
        output out[];
}