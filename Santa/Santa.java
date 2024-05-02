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
    private JLabel santaLabel, elfLabel, reindeerLabel;
    private JLabel santaAction, elfAction, reindeerAction;
    private ImageIcon sleepingSanta, helpingElves, preparingSleigh, elfNeedHelp, reindeerOnVacation, reindeerReturned;
    private ScheduledExecutorService executor;

    public Santa() {
        // Cargar las imágenes
        sleepingSanta = new ImageIcon(new ImageIcon("C:/Users/uriel/Desktop/Santa/dormir.jpg").getImage().getScaledInstance(400, 400, Image.SCALE_SMOOTH));
        helpingElves = new ImageIcon(new ImageIcon("C:/Users/uriel/Desktop/Santa/ayudando.jpeg").getImage().getScaledInstance(400, 400, Image.SCALE_SMOOTH));
        preparingSleigh = new ImageIcon(new ImageIcon("C:/Users/uriel/Desktop/Santa/trineo2.jpeg").getImage().getScaledInstance(400, 400, Image.SCALE_SMOOTH));
        elfNeedHelp = new ImageIcon(new ImageIcon("C:/Users/uriel/Desktop/Santa/ayuda.jpeg").getImage().getScaledInstance(400, 400, Image.SCALE_SMOOTH));
        reindeerOnVacation = new ImageIcon(new ImageIcon("C:/Users/uriel/Desktop/Santa/vacaciones.jpeg").getImage().getScaledInstance(400, 400, Image.SCALE_SMOOTH));
        reindeerReturned = new ImageIcon(new ImageIcon("C:/Users/uriel/Desktop/Santa/regresando.jpeg").getImage().getScaledInstance(400, 400, Image.SCALE_SMOOTH));
        ImageIcon fondo = new ImageIcon("C:/Users/uriel/Desktop/Santa/fondo.jpg");
        
              // Crear la GUI
        JFrame frame = new JFrame("Simulación de Santa Claus");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(600, 600);

        santaLabel = new JLabel(sleepingSanta);
        elfLabel = new JLabel(elfNeedHelp);
        reindeerLabel = new JLabel(reindeerOnVacation);

        santaAction = new JLabel("Santa Claus está durmiendo...");
        elfAction = new JLabel("Los duendes están trabajando...");
        reindeerAction = new JLabel("Los renos están de vacaciones...");

        JPanel santaPanel = new JPanel(new BorderLayout());
        santaPanel.add(santaLabel, BorderLayout.CENTER);
        santaPanel.add(santaAction, BorderLayout.SOUTH);

        JPanel elfPanel = new JPanel(new BorderLayout());
        elfPanel.add(elfLabel, BorderLayout.CENTER);
        elfPanel.add(elfAction, BorderLayout.SOUTH);

        JPanel reindeerPanel = new JPanel(new BorderLayout());
        reindeerPanel.add(reindeerLabel, BorderLayout.CENTER);
        reindeerPanel.add(reindeerAction, BorderLayout.SOUTH);

        JPanel panel = new JPanel(new GridLayout(1, 3));
        panel.add(santaPanel);
        panel.add(elfPanel);
        panel.add(reindeerPanel);
        frame.getContentPane().add(panel, BorderLayout.CENTER);

        JButton endButton = new JButton("Finalizar");
        endButton.addActionListener(e -> endSimulation());
        frame.getContentPane().add(endButton, BorderLayout.SOUTH);

        frame.setVisible(true);
    }

    public void startSimulation() {
        executor = Executors.newScheduledThreadPool(1);

        // Simular que los renos regresan de vacaciones después de un tiempo
        executor.scheduleAtFixedRate(() -> {
            if (reindeerCount < TOTAL_REINDEER) {
                reindeerCount++;
                reindeerLabel.setIcon(reindeerReturned);
                reindeerAction.setText(reindeerCount + " reno(s) ha(n) vuelto de vacaciones.");
                checkConditions();
            }
        }, 0, 3, TimeUnit.SECONDS);

        // Simular que los duendes necesitan ayuda después de un tiempo
        executor.scheduleAtFixedRate(() -> {
            if (elvesWaiting < TOTAL_ELVES) {
                elvesWaiting++;
                elfLabel.setIcon(elfNeedHelp);
                elfAction.setText(elvesWaiting + " duende(s) necesita(n) ayuda.");
                checkConditions();
            }
        }, 0, 5, TimeUnit.SECONDS);
    }

    public void endSimulation() {
        executor.shutdown();
        santaAction.setText("La simulación ha terminado.");
    }

    public synchronized void checkConditions() {
        if (reindeerCount == TOTAL_REINDEER) {
            santaLabel.setIcon(preparingSleigh);
            santaAction.setText("Santa Claus está preparando el trineo y repartiendo los regalos.");
            try {
                Thread.sleep(10000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            santaLabel.setIcon(sleepingSanta);
            santaAction.setText("Santa Claus ha terminado y está descansando nuevamente.");
            reindeerLabel.setIcon(reindeerOnVacation);
            reindeerAction.setText("Los renos están de vacaciones.");
            reindeerCount = 0;
        } else if (elvesWaiting == TOTAL_ELVES) {
            santaLabel.setIcon(helpingElves);
            santaAction.setText("Santa Claus está ayudando a los duendes con sus problemas.");
            try {
                Thread.sleep(10000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            santaLabel.setIcon(sleepingSanta);
            santaAction.setText("Santa Claus ha terminado de ayudar a los duendes y está descansando nuevamente.");
            elfLabel.setIcon(elfNeedHelp);
            elfAction.setText("Los duendes están trabajando...");
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
