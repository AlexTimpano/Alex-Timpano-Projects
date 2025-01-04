using OxyPlot.Series;
using OxyPlot.WindowsForms;
using OxyPlot;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using org.mariuszgromada.math.mxparser;

namespace Quickcalc
{
    public partial class Calculator : Form
    {
        public Calculator()
        {
            InitializeComponent();
        }

        private float leftValue = 0;
        private float rightValue = 10;
        private float stepValue = 1;
        private string equation;

        private PlotView pv = new PlotView();
        private FunctionSeries fs = new FunctionSeries();

        private void Calculator_Load(object sender, EventArgs e)
        {
            pv.Location = new Point(0, 0);
            pv.Size = new Size(800, 400);
            this.Controls.Add(pv);
            pv.Model = new PlotModel { Title = " " };

            fs.Points.Add(new DataPoint(0, 0));
            fs.Points.Add(new DataPoint(1, 1));
            pv.Model.Series.Add(fs);
          

        }

        private void leftInterval_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (!char.IsControl(e.KeyChar) && !char.IsDigit(e.KeyChar) && e.KeyChar != '.' && e.KeyChar != '-')
            {
                e.Handled = true;
            }

            // only allow one decimal point
            if (e.KeyChar == '.' && (sender as TextBox).Text.IndexOf('.') > -1)
            {
                e.Handled = true;
            }

            // only allow one negative sign
            if (e.KeyChar == '-' && ((sender as TextBox).Text.IndexOf('-') > -1 || (sender as TextBox).Text.Length > 0))
            {
                e.Handled = true;
            }
        }


        private void rightInterval_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (!char.IsControl(e.KeyChar) && !char.IsDigit(e.KeyChar) && e.KeyChar != '.' && e.KeyChar != '-')
            {
                e.Handled = true;
            }

            // only allow one decimal point
            if (e.KeyChar == '.' && (sender as TextBox).Text.IndexOf('.') > -1)
            {
                e.Handled = true;
            }

            // only allow one negative sign
            if (e.KeyChar == '-' && ((sender as TextBox).Text.IndexOf('-') > -1 || (sender as TextBox).Text.Length > 0))
            {
                e.Handled = true;
            }
        }

        private void stepBox_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (!char.IsControl(e.KeyChar) && !char.IsDigit(e.KeyChar) && e.KeyChar != '.')
            {
                e.Handled = true;
            }

            // only allow one decimal point
            if (e.KeyChar == '.' && (sender as TextBox).Text.IndexOf('.') > -1)
            {
                e.Handled = true;
            }
        }

        private void leftInterval_TextChanged(object sender, EventArgs e)
        {
            float.TryParse(leftInterval.Text, out leftValue);
           
        }

        private void rightInterval_TextChanged(object sender, EventArgs e)
        {
            float.TryParse(rightInterval.Text, out rightValue);
        }

        private void stepBox_TextChanged(object sender, EventArgs e)
        {
            float.TryParse(stepBox.Text, out stepValue);
        }

        private void graphButton_Click(object sender, EventArgs e)
        {
            pv.Model.Series.Clear();

            fs.Points.Clear();



            Expression expression = new Expression(equation);


            if (leftValue < rightValue && stepValue>0) 
            {
                errorBox.Visible = false;
                for (float i = leftValue; i <= rightValue; i += stepValue)
                {
                    expression.removeAllArguments();
                    expression.addArguments(new Argument("x", i));

                    double result = expression.calculate();



                    if (!double.IsNaN(result))
                    {
                        fs.Points.Add(new DataPoint(i, result));
                    }

                    else
                    {
                        fs.Points.Add(new DataPoint(i, double.NaN));
                    }

                }
            }



            else if(leftValue>=rightValue)
            {
                errorBox.Visible = true;
                errorBox.Text = "ERROR: Left interval must be less than right interval";
            }

            else
            {
                errorBox.Visible = true;
                errorBox.Text = "ERROR: Step value must be greater than 0";
            }
            

            pv.Model.Series.Add(fs);
          
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {
            equation = textBox1.Text;
        }
    }
}
