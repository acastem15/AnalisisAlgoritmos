import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.Set;

/**
 * Clase principal que:
 * 1) Lee un archivo CSV (origen,destino,costo).
 * 2) Construye un grafo no dirigido.
 * 3) Ejecuta el algoritmo de Prim para obtener el Árbol de Recubrimiento Mínimo (MST). 
 * En este caso de uso (calles dentro de una ciudad),  donde se espera que el grafo esté densamente 
 * conectado con muchas aristas, el algoritmo de Prim resulta más eficiente que el de Kruskal. 
 * Esto se debe a que Kruskal es más adecuado para grafos dispersos, ya que requiere ordenar todas las 
 * aristas del grafo.
 */
public class PrimAlgorithm {

    // Estructura para representar una arista en la lista de adyacencia
    // En este caso, solo necesitamos saber el nodo destino y el peso.
    static class Edge {
        String destino;
        double costo;

        public Edge(String destino, double costo) {
            this.destino = destino;
            this.costo = costo;
        }
    }

    /**
     * Ejecuta el algoritmo de Prim sobre un grafo no dirigido.
     *
     * @param grafo      Mapa: nombreDelNodo -> lista de aristas (destino, peso)
     * @param nodoInicio El nodo donde empieza Prim.
     * @return Costo total del Árbol de Recubrimiento Mínimo (MST).
     */
    public static double primMST(Map<String, List<Edge>> grafo, String nodoInicio) {
        // Conjunto para marcar nodos visitados
        Set<String> visitados = new HashSet<>();

        List<AristaMST> mst = new ArrayList<>();
        

        // Cola de prioridad (min-heap) basada en el costo de la arista
        // Guardamos tuplas (costo, nodoOrigen, nodoDestino) para referencia
        // Complejidad de PriorityQueue: O(log n) para insertar y extraer el mínimo. Y O(1) para recuperar.
        // Implementación basada en un heap binario.
        PriorityQueue<AristaMST> pq = new PriorityQueue<>(Comparator.comparingDouble(a -> a.costo));

        // Añadimos las aristas que salen del nodo de inicio
        visitados.add(nodoInicio);
        for (Edge arista : grafo.get(nodoInicio)) {
            pq.offer(new AristaMST(nodoInicio, arista.destino, arista.costo));
        }

        double costoTotal = 0.0;

        // Mientras haya aristas candidatas y falten nodos por visitar
        while (!pq.isEmpty() && (visitados.size() < grafo.size())) {
            // Extraer la arista de menor costo
            AristaMST arista = pq.poll();
            String destino = arista.nodoDestino;

            // Si ya visitamos el nodo destino, ignoramos esta arista
            if (visitados.contains(destino)) {
                continue;
            }

            // Agregamos esta arista al MST
            visitados.add(destino);
            costoTotal += arista.costo;
            mst.add(arista);

            // Agregamos las aristas que salen de 'destino'
            for (Edge e : grafo.getOrDefault(destino, new ArrayList<>())) {
                if (!visitados.contains(e.destino)) {
                    pq.offer(new AristaMST(destino, e.destino, e.costo));
                }
            }
        }

        System.out.println("****** MST ******");
            for (AristaMST a : mst) {
                System.out.println(a.nodoOrigen + " -> " + a.nodoDestino + " : " + a.costo);
            }



        return costoTotal;
    }

    // Clase interna para guardar la información cuando usamos la PriorityQueue
    static class AristaMST {
        String nodoOrigen;
        String nodoDestino;
        double costo;

        public AristaMST(String nodoOrigen, String nodoDestino, double costo) {
            this.nodoOrigen = nodoOrigen;
            this.nodoDestino = nodoDestino;
            this.costo = costo;
        }
    }

    public static void main(String[] args) throws Exception {
        if (args.length < 1) {
            System.err.println("Uso: java PrimAlgorithm <nombreDeArchivo.csv>");
            System.exit(1);
        }
        String filename = args[0];

        // 1) Leer el archivo y construir el grafo
        Map<String, List<Edge>> grafo = new HashMap<>();
        List<String> nodos = new ArrayList<>(); // Guardará nodos en orden de aparición

        try (FileReader reader = new FileReader(filename);
             BufferedReader in = new BufferedReader(reader)) {

            String line = in.readLine();
            // Asumimos que la primera línea es la cabecera: "origen,destino,costo"
            // Si no fuese tu caso, simplemente comenta o elimina este primer 'readLine()'.
            // O verifica si la línea contiene algo como "origen" para saltártela.
            if (line != null && line.startsWith("origen")) {
                // Ya la saltamos
                line = in.readLine();
            }

            while (line != null) {
                // Formato esperado: "Bogotá,Medellín,6"
                String[] parts = line.split(",");
                if (parts.length == 3) {
                    String origen = parts[0].trim();
                    String destino = parts[1].trim();
                    double costo = Double.parseDouble(parts[2].trim());

                    // Añadir a la lista de nodos si no existe
                    // Dado que el propósito es convertir las calles en doble sentido,
                    // se agregan las aristas en ambas direcciones. De esta forma,
                    // se garantiza que el MST identifique las calles que deben construirse.
                    if (!grafo.containsKey(origen)) {
                        grafo.put(origen, new ArrayList<>());
                        nodos.add(origen);
                    }
                    if (!grafo.containsKey(destino)) {
                        grafo.put(destino, new ArrayList<>());
                        nodos.add(destino);
                    }

                    // Aristas en ambas direcciones (grafo No dirigido)
                    grafo.get(origen).add(new Edge(destino, costo));
                    grafo.get(destino).add(new Edge(origen, costo));
                }
                line = in.readLine();
            }
        }

        // 2) Ejecutar Prim. Tomamos como nodo inicial el primero de la lista 'nodos'
        //   (Podrías elegir cualquier otro si así lo deseas)
        if (nodos.isEmpty()) {
            System.out.println("El archivo no contiene datos válidos.");
            return;
        }
        String nodoInicio = nodos.get(0);
        double costoMST = primMST(grafo, nodoInicio);

        // 3) Mostrar resultado
        System.out.println("\nNodo inicial: " + nodoInicio);

        System.out.println("\nCosto total del Árbol de Recubrimiento Mínimo (MST): " + costoMST);
    }
}
