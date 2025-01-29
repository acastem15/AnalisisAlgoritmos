public class Nodo {

    private int id; 
    private int color=-1;   

    public Nodo(int id) {
        this.id = id; 
    }
    @Override
    public String toString() {
        return "Nodo [id=" + id + ", color=" + color + "]";
    }

    //Getter - Setter
    public int getId() {
        return id;
    }
    public int getColor() {
        return color;
    }

    public void setColor(int color) {
        this.color = color;
    }


}
