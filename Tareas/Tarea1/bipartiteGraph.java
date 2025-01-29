import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Queue;
import java.util.Random;

public class bipartiteGraph {
    public static void main(String[] args) throws Exception {
        Parser parser = new Parser(); 
        //Get filename
        //Scanner inputObj = new Scanner(System.in);  
        //String fileName = inputObj.nextLine(); 

        //Adjacency List
        //String currentPath = new java.io.File(".").getCanonicalPath();
        ArrayList<ArrayList<Nodo>> adjacencyList = parser.createAdjacencyList(); 
        ArrayList<Nodo> nodes=parser.getNodeList();

        //Bipartite graph algorithm

        boolean isBipartite = bipartiteGraph(nodes,adjacencyList);
        System.out.println(isBipartite);
        
        
    
        }
        
        
    public static Boolean bipartiteGraph(ArrayList<Nodo> notVisited , ArrayList<ArrayList<Nodo>> graph){
        boolean isBipartite = true; 
        Random rand = new Random(); 
        Queue<Nodo> queue = new ArrayDeque<>();
        int nextColor = 0; 

        while ((!notVisited.isEmpty()) && isBipartite){
            int randomID= rand.nextInt(notVisited.size());
            Nodo initialNode = notVisited.get(randomID); 
            queue.add(initialNode); 

            while (!queue.isEmpty() && isBipartite){

                try{
                    //Get from queue
                    Nodo currentNode=queue.remove();

                    //Remove from not visited
                    notVisited.remove(currentNode); 

                    //Color node if it does not have color
                    if (currentNode.getColor() <0){

                    
                    currentNode.setColor(nextColor);
                    }
                    //Get current color
                    int colorCurrentNode = currentNode.getColor(); 

                    nextColor = (colorCurrentNode+1)%2; //Alternate between 0 and 1

                    ArrayList<Nodo> adjacents = graph.get(currentNode.getId()); 

                    for (Nodo adNode : adjacents) {
                        int colorAdNod= adNode.getColor(); 
                        if (colorAdNod<0){
                            queue.add(adNode); 
                            adNode.setColor(nextColor);
                        }
                        else if (colorAdNod != nextColor){
                            isBipartite=false; 
                        }
                        
                    }

                }catch(Exception e) {
                    System.out.println("Bipartite graph algorithm not working");
                    e.printStackTrace();
                }

                


            }



        }




        return isBipartite;
    }





}
