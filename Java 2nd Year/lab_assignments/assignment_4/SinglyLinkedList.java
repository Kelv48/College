    class Node {
        int data;
        Node next;

        public Node(int d) {
            data = d;
            next = null;
        }
    }

    public class SinglyLinkedList {
        Node head;

     public SinglyLinkedList() {
        this.head = null;
     }   

     public void add_first(int data) {
        Node newNode = new Node(data);
        newNode.next = head;
        head = newNode;
     }

     public void add_last(int data) {
        Node newNode = new Node(data);
        if (head == null) {
            head = newNode;
            return;
        } else {
            Node last = head;
            while(last.next != null) {
                last = last.next;
            }
            last.next = newNode;
        }
     }
     
     public void remove_first_item() {
        if (head == null) {
            return;
        } else {
            head = head.next;
        }
    }

    public void remove_last_item() {
        if (head == null) {
            return;
        } else if (head.next == null) {
            head = null;
            return;
        } else {
            Node secondLast = head;
            while (secondLast.next.next != null) {
                secondLast = secondLast.next;
            }
           secondLast.next = null; 
        }
    }

    public void insert(int data) {
        Node newNode = new Node(data);
        if (head == null) {
            head = newNode;
        } else {
            Node last = head;
            while (last.next != null) {
                last = last.next;
            }
            last.next = newNode;
        }
    }

    public void insertAtPosition(int data, int position) {
        Node newNode = new Node(data);
        if (position == 1) {
            newNode.next = head;
            head = newNode;
            return;
        }
        Node current = head;
        for (int i = 1; i < position - 1 && current != null; i++) {
            current = current.next;
        }
        if (current == null) {
            System.out.println("Invalid position");
        } else {
            newNode.next = current.next;
            current.next = newNode;
        }
    }

    // Method to delete a node at a specific position
    public void deleteAtPosition(int position) {
        if (position == 1) {
            head = head.next;
            return;
        }
        Node current = head;
        Node previous = null;
        for (int i = 1; i < position && current != null; i++) {
            previous = current;
            current = current.next;
        }
        if (current == null) {
            System.out.println("Invalid position");
        } else {
            previous.next = current.next;
        }
    }

    public void printList() {
        Node current = head;
        while (current != null) {
            System.out.print(current.data + " ");
            current = current.next;
        }
        System.out.println();
    }

    public static void main(String[] args) {
        SinglyLinkedList myList = new SinglyLinkedList();

        myList.insert(11);
        myList.insert(22);
        myList.insert(6);
        myList.insert(89);
        myList.insert(99);

        // Printing the initial linked list
        System.out.println("Initial linked list:");
        myList.printList();

        // Inserting a number at the third position
        myList.insertAtPosition(50, 3);
        System.out.println("Linked list after inserting 50 at position 3:");
        myList.printList();

        // Deleting the 2nd element
        myList.deleteAtPosition(2);
        System.out.println("Linked list after deleting element at position 2:");
        myList.printList();

        // Deleting the 1st element
        myList.deleteAtPosition(1);
        System.out.println("Linked list after deleting element at position 1:");
        myList.printList();

        // Deleting the last element
        myList.deleteAtPosition(4); // Since the list has 4 elements now
        System.out.println("Linked list after deleting last element:");
        myList.printList();

    }
}
