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


simple Source
{
    parameters:
        @group(Queueing);
        @signal[created](type="long");
        @statistic[created](title="il numero di job creati"; record=last;interpolationmode=none);
        
       @display("i=block/source");
       
       // numero di job da generare (-1 senza limite)
       int numJobs = default(-1);
       
       // parametro per il tempo di interarrivo dei job
       volatile double lambda;
       
       string jobName = default("job");
       
       double startTime = default(lambda); 		// Quando il modulo invia il primo lavoro
       double stopTime @unit(s) = default(-1s); // quando il modulo interrompe la generazione del lavoro (-1 significa nessun limite)
   gates:
       output out;
}