import java.awt.event.AdjustmentListener;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class Parser {

    ArrayList<Nodo> nodeList; 
    

        
        public ArrayList<Nodo> getNodeList() {
        return nodeList;
    }

        public Parser() {
            this.nodeList =  new ArrayList<Nodo>();
        }

        private void addEdge(ArrayList<ArrayList<Nodo>> adjList, int n1,int n2){
            Nodo nodo = this.nodeList.get(n2);
            adjList.get(n1).add(nodo); 
    
        }
    
        public ArrayList<ArrayList<Nodo>> createAdjacencyList() throws IOException{

            ArrayList<ArrayList<Nodo>> adjacencyList = new ArrayList<>(); 
            InputStreamReader inReader= new InputStreamReader(System.in); 
            BufferedReader reader = new BufferedReader(inReader);
            
            try {
       
                int numNodes;
                numNodes = Integer.parseInt(reader.readLine());
                

                //Node list creation
                for (int i = 0; i < numNodes; i++) {
                    this.nodeList.add(new Nodo(i)); 
                    adjacencyList.add(new ArrayList<>());
                }
                //Input parser
                String line;
                while ((line = reader.readLine()) != null) {
                    String[] fight = line.split(" ");
                    int nid1= Integer.parseInt(fight[0]);
                    int nid2 = Integer.parseInt(fight[1]);
                    addEdge(adjacencyList,nid1,nid2); 
                    addEdge(adjacencyList,nid2,nid1); 
                }

                reader.close();
                
            } catch (FileNotFoundException e) {
                System.out.println("Error in adjacency list creation.");
                e.printStackTrace();
            }
            return adjacencyList;
    }

}
