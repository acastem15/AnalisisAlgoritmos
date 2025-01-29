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

public class PrimAlgorithm {

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
        Set<String> visitados = new HashSet<>();
        List<AristaMST> mst = new ArrayList<>();

        PriorityQueue<AristaMST> pq = new PriorityQueue<>(Comparator.comparingDouble(a -> a.costo));

        visitados.add(nodoInicio);
        for (Edge arista : grafo.get(nodoInicio)) {
            pq.offer(new AristaMST(nodoInicio, arista.destino, arista.costo));
        }

        double costoTotal = 0.0;

        while (!pq.isEmpty() && (visitados.size() < grafo.size())) {
            AristaMST arista = pq.poll();
            String destino = arista.nodoDestino;

            if (visitados.contains(destino)) {
                continue;
            }

            visitados.add(destino);
            costoTotal += arista.costo;
            mst.add(arista);

            for (Edge e : grafo.getOrDefault(destino, new ArrayList<>())) {
                if (!visitados.contains(e.destino)) {
                    pq.offer(new AristaMST(destino, e.destino, e.costo));
                }
            }
        }

        System.out.println("Calles Elegidas para Conversión a Doble Vía");
            for (AristaMST a : mst) {
                System.out.println(a.nodoOrigen + " a " + a.nodoDestino + " (costo: " + a.costo+")");
            }



        return costoTotal;
    }

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

        Map<String, List<Edge>> grafo = new HashMap<>();
        List<String> nodos = new ArrayList<>(); 

        try (FileReader reader = new FileReader(filename);
             BufferedReader in = new BufferedReader(reader)) {

            String line = in.readLine();

            while (line != null) {
                String[] parts = line.split(",");
                if (parts.length == 3) {
                    String origen = parts[0].trim();
                    String destino = parts[1].trim();
                    double costo = Double.parseDouble(parts[2].trim());

                    if (!grafo.containsKey(origen)) {
                        grafo.put(origen, new ArrayList<>());
                        nodos.add(origen);
                    }
                    if (!grafo.containsKey(destino)) {
                        grafo.put(destino, new ArrayList<>());
                        nodos.add(destino);
                    }

                    grafo.get(origen).add(new Edge(destino, costo));
                    grafo.get(destino).add(new Edge(origen, costo));
                }
                line = in.readLine();
            }
        }

        if (nodos.isEmpty()) {
            System.out.println("El archivo no contiene datos válidos.");
            return;
        }
        String nodoInicio = nodos.get(0);
        double costoMST = primMST(grafo, nodoInicio);

        System.out.println("\nCosto total del proyecto: " + costoMST);
    }
}
