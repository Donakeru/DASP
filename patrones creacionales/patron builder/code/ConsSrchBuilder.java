import java.io.*;
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import com.sun.java.swing.plaf.windows.*;
import java.util.*;

class ConsSrchBuilder extends UIBuilder {

  private JTextField txtAddress = new JTextField(20);
  private JTextField txtIdNumber = new JTextField(15);
  private JTextField txtEmail = new JTextField(20);
  private JTextField txtExperienceYears = new JTextField(5);
  private JTextField txtPhoneNumber = new JTextField(15);

  public void addUIControls() {

    searchUI = new JPanel();

    JLabel lblAddress = new JLabel("Address:");
    JLabel lblIdNumber = new JLabel("Identification Number:");
    JLabel lblEmail = new JLabel("E-mail:");
    JLabel lblExperienceYears = new JLabel("Experience years:");
    JLabel lblPhoneNumber = new JLabel("Phone number:");

    GridBagLayout gridbag = new GridBagLayout();
    searchUI.setLayout(gridbag);

    GridBagConstraints gbc = new GridBagConstraints();

    searchUI.add(lblAddress);
    searchUI.add(txtAddress);
    searchUI.add(lblIdNumber);
    searchUI.add(txtIdNumber);
    searchUI.add(lblEmail);
    searchUI.add(txtEmail);
    searchUI.add(lblExperienceYears);
    searchUI.add(txtExperienceYears);
    searchUI.add(lblPhoneNumber);
    searchUI.add(txtPhoneNumber);

    gbc.anchor = GridBagConstraints.WEST;

    gbc.insets.top = 5;
    gbc.insets.bottom = 5;
    gbc.insets.left = 5;
    gbc.insets.right = 5;

    gbc.gridx = 0;
    gbc.gridy = 0;
    gridbag.setConstraints(lblAddress, gbc);

    gbc.gridx = 0;
    gbc.gridy = 1;
    gridbag.setConstraints(lblIdNumber, gbc);

    gbc.gridx = 0;
    gbc.gridy = 2;
    gridbag.setConstraints(lblEmail, gbc);

    gbc.gridx = 0;
    gbc.gridy = 3;
    gridbag.setConstraints(lblExperienceYears, gbc);

    gbc.gridx = 0;
    gbc.gridy = 4;
    gridbag.setConstraints(lblPhoneNumber, gbc);

    gbc.gridx = 1;
    gbc.gridy = 0;
    gridbag.setConstraints(txtAddress, gbc);

    gbc.gridx = 1;
    gbc.gridy = 1;
    gridbag.setConstraints(txtIdNumber, gbc);

    gbc.gridx = 1;
    gbc.gridy = 2;
    gridbag.setConstraints(txtEmail, gbc);

    gbc.gridx = 1;
    gbc.gridy = 3;
    gridbag.setConstraints(txtExperienceYears, gbc);

    gbc.gridx = 1;
    gbc.gridy = 4;
    gridbag.setConstraints(txtPhoneNumber, gbc);
  }

  public void initialize() {

    txtAddress.setText("Enter Address");
    txtIdNumber.setText("Enter Identification Number");
    txtEmail.setText("Enter E-mail");
    txtExperienceYears.setText("0");
    txtPhoneNumber.setText("Enter Phone number");

  }

  public String getSQL() {

    return ("SELECT * FROM Consultant WHERE Address='" +
      txtAddress.getText() + "'" +
      " AND IdentificationNumber='" +
      txtIdNumber.getText() + "'" +
      " AND Email='" +
      txtEmail.getText() + "'" +
      " AND ExperienceYears='" +
      txtExperienceYears.getText() + "'" +
      " AND PhoneNumber='" +
      txtPhoneNumber.getText() + "'");

  }

}