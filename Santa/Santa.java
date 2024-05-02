/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package santa;

/**
 *
 * @author uriel
 */
import javax.swing.*;
import java.awt.*;
import java.util.concurrent.*;

public class Santa {
    private static final int TOTAL_REINDEER = 9;
    private static final int TOTAL_ELVES = 3;
    private int reindeerCount = 0;
    private int elvesWaiting = 0;
    private JLabel statusLabel;
    private ImageIcon sleepingSanta;
    private ImageIcon helpingElves;
    private ImageIcon preparingSleigh;

    public Santa() {
        // Cargar las imágenes
        sleepingSanta = new ImageIcon("dormir.jpg");
        helpingElves = new ImageIcon("ayudando.jpeg");
        preparingSleigh = new ImageIcon("trineo2.jpeg");

        // Crear la GUI
        JFrame frame = new JFrame("Simulación de Santa Claus");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 400);

        statusLabel = new JLabel("Santa Claus está durmiendo...", sleepingSanta, JLabel.CENTER);
        frame.getContentPane().add(statusLabel, BorderLayout.CENTER);

        frame.setVisible(true);
    }

    public void startSimulation() {
        ScheduledExecutorService executor = Executors.newScheduledThreadPool(1);

        // Simular que los renos regresan de vacaciones después de un tiempo
        executor.schedule(() -> {
            reindeerCount = TOTAL_REINDEER;
            checkConditions();
        }, 3, TimeUnit.SECONDS);

        // Simular que los duendes necesitan ayuda después de un tiempo
        executor.scheduleAtFixedRate(() -> {
            elvesWaiting++;
            checkConditions();
        }, 5, 5, TimeUnit.SECONDS);

        // Detener la ejecución después de un minuto y medio
        executor.schedule(() -> {
            executor.shutdown();
        }, 40, TimeUnit.SECONDS);
    }

    public synchronized void checkConditions() {
        if (reindeerCount == TOTAL_REINDEER) {
            statusLabel.setText("Santa Claus está preparando el trineo y repartiendo los regalos.");
            statusLabel.setIcon(preparingSleigh);
            try {
                Thread.sleep(10000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            statusLabel.setText("Santa Claus ha terminado y está descansando nuevamente.");
            statusLabel.setIcon(sleepingSanta);
            reindeerCount = 0;
        } else if (elvesWaiting >= TOTAL_ELVES) {
            statusLabel.setText("Santa Claus está ayudando a los duendes con sus problemas.");
            statusLabel.setIcon(helpingElves);
            try {
                Thread.sleep(10000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            statusLabel.setText("Santa Claus ha terminado de ayudar a los duendes y está descansando nuevamente.");
            statusLabel.setIcon(sleepingSanta);
            elvesWaiting = 0;
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            Santa santa = new Santa();
            santa.startSimulation();
        });
    }
}
