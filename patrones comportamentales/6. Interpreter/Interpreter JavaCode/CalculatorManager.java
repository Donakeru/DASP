import java.io.*;
import java.io.*;
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import com.sun.java.swing.plaf.windows.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class CalculatorManager extends JFrame {
  public static final String CALCULATE = "Calculate";
  public static final String EXIT = "Exit";

  private JTextField txtExpression;
  public JLabel lblResult, lblResultValue;

  public CalculatorManager() {
    super("Calculadora");

    txtExpression = new JTextField(20);

    lblResult = new JLabel("Resultado:");
    lblResultValue = new JLabel("0");

    // Create the calculate button
    JButton CalculateButton = new JButton(CalculatorManager.CALCULATE);

    CalculateButton.setMnemonic(KeyEvent.VK_E);
    JButton exitButton = new JButton(CalculatorManager.EXIT);
    exitButton.setMnemonic(KeyEvent.VK_X);
    ButtonHandler objButtonHandler = new ButtonHandler(this);

    CalculateButton.addActionListener(objButtonHandler);
    exitButton.addActionListener(new ButtonHandler());

    JPanel buttonPanel = new JPanel();

    // ****************************************************
    GridBagLayout gridbag = new GridBagLayout();
    buttonPanel.setLayout(gridbag);
    GridBagConstraints gbc = new GridBagConstraints();

    buttonPanel.add(txtExpression);
    buttonPanel.add(lblResult);
    buttonPanel.add(lblResultValue);

    buttonPanel.add(CalculateButton);
    buttonPanel.add(exitButton);

    gbc.insets.top = 5;
    gbc.insets.bottom = 5;
    gbc.insets.left = 5;
    gbc.insets.right = 5;

    gbc.anchor = GridBagConstraints.WEST;
    gbc.gridx = 0;
    gbc.gridy = 0;
    gbc.gridwidth = 2;
    gridbag.setConstraints(txtExpression, gbc);
    gbc.gridwidth = 1;
    gbc.anchor = GridBagConstraints.EAST;
    gbc.gridx = 0;
    gbc.gridy = 1;
    gridbag.setConstraints(lblResult, gbc);
    gbc.anchor = GridBagConstraints.WEST;
    gbc.gridx = 1;
    gbc.gridy = 1;
    gridbag.setConstraints(lblResultValue, gbc);

    gbc.insets.left = 2;
    gbc.insets.right = 2;
    gbc.insets.top = 40;
    gbc.anchor = GridBagConstraints.EAST;

    gbc.gridx = 0;
    gbc.gridy = 5;
    gridbag.setConstraints(CalculateButton, gbc);
    gbc.anchor = GridBagConstraints.WEST;
    gbc.gridx = 1;
    gbc.gridy = 5;
    gridbag.setConstraints(exitButton, gbc);

    // ****************************************************

    // Add the buttons and the log to the frame
    Container contentPane = getContentPane();

    contentPane.add(buttonPanel, BorderLayout.CENTER);
    try {
      UIManager.setLookAndFeel(new WindowsLookAndFeel());
      SwingUtilities.updateComponentTreeUI(
          CalculatorManager.this);
    } catch (Exception ex) {
      System.out.println(ex);
    }

  }

  public static void main(String[] args) {
    JFrame frame = new CalculatorManager();

    frame.addWindowListener(new WindowAdapter() {
      public void windowClosing(WindowEvent e) {
        System.exit(0);
      }
    });

    // frame.pack();
    frame.setSize(400, 300);
    frame.setVisible(true);
  }

  public String getExpression() {
    return txtExpression.getText();
  }

  public void setResult(String searchResult) {
    lblResultValue.setText(searchResult);
  }

} // End of class CalculatorManager

class ButtonHandler implements ActionListener {
  CalculatorManager objCalculatorManager;

  public void actionPerformed(ActionEvent e) {

    if (e.getActionCommand().equals(CalculatorManager.EXIT)) {
      System.exit(1);
    }
    if (e.getActionCommand().equals(CalculatorManager.CALCULATE)) {

      Calculator calc = new Calculator();
      // instantiate the context
      Context ctx = new Context();

      String expression = objCalculatorManager.getExpression();

      int asciiValue = 97;
      Pattern p = Pattern.compile("[0-9]+");
      Matcher m = p.matcher(expression.replace(" ", ""));
      StringBuffer sb = new StringBuffer();
      while (m.find()) {
        try {
          int numero = Integer.parseInt(m.group());
          String letra = String.valueOf((char) asciiValue);
          m.appendReplacement(sb, letra);
          ctx.assign(letra, numero);
          asciiValue++;
        } catch (Exception exp) {
          System.out.println("mal");
        }
      }
      m.appendTail(sb);

      String inFix = sb.toString();

      // set the expression to evaluate
      calc.setExpression(inFix);

      // configure the calculator with the Context
      calc.setContext(ctx);

      try {
        int resultado = calc.evaluate();
        // Display the result
        objCalculatorManager.setResult(String.valueOf(resultado));
      } catch (ArithmeticException exc) {
        objCalculatorManager.setResult("Error matemático");
      } catch (NullPointerException exc) {
        objCalculatorManager.setResult("Error de sintaxis");
      }

    }

  }

  public ButtonHandler() {
  }

  public ButtonHandler(CalculatorManager inObjCalculatorManager) {
    objCalculatorManager = inObjCalculatorManager;
  }

} // End of class ButtonHandler
