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

// Dichiarazione del network che collega tutti i nodi
network HeavyTrafficLimits
{
    submodules:
        source: Source {
            @display("p=50,50");
        }
        queue1: PassiveQueue {
            @display("p=170,50");
        }
        server1: Server {
            @display("p=258,50");
        }
        queue2: PassiveQueue {
            @display("p=258,150");
        }
        server2: Server {
            @display("p=170,150");
        }
        queue3: PassiveQueue {
            @display("p=268,246");
        }
        server3: Server {
            @display("p=170,246");
        }
        router: Router {
            @display("p=384,189");
        }
        //queue: Queue {
            //@display("p=112,189");
        //}
        sink: Sink {
            @display("p=50,189");
        }
    connections:
        source.out --> queue1.in++;
        queue1.out++ --> server1.in++;
        server1.out --> router.in;
        router.out[0] --> queue2.in++;
        router.out[1] --> queue3.in++;
        queue2.out++ --> server2.in++;
        queue3.out++ --> server3.in++;
        server2.out --> sink.in++;
        server3.out --> sink.in++;

        //server2.out --> queue.in++;
        //server3.out --> queue.in++;
        //queue.out --> sink.in++;

        //source.out --> server1.in++;
        //server1.out --> router.in;
        //router.out[0] --> server2.in++;
        //router.out[1] --> server3.in++;
        //server2.out --> sink.in[0];
        //server3.out --> sink.in[1];
}
