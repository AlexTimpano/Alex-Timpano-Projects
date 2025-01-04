using org.mariuszgromada.math.mxparser;
using OxyPlot;
using OxyPlot.Series;
using OxyPlot.WindowsForms;

namespace Quickcalc
{
    public partial class Form1 : Form
    {


        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private String expressionString = "";
        private List<String> expressionList = new List<String>();
        private bool shift = false;
        private bool alpha = false;

       

        private void button1_Click(object sender, EventArgs e)
        {
            expressionList.Add("1");
            expressionString = String.Join("", expressionList);
            inputLabel.Text= expressionString;  
        }

        private void button2_Click(object sender, EventArgs e)
        {
            expressionList.Add("2");
            expressionString = String.Join("", expressionList);
            inputLabel.Text = expressionString;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            expressionList.Add("3");
            expressionString = String.Join("", expressionList);
            inputLabel.Text = expressionString;
        }

        private void button4_Click(object sender, EventArgs e)
        {
            expressionList.Add("4");
            expressionString = String.Join("", expressionList);
            inputLabel.Text = expressionString;
        }

        private void button5_Click(object sender, EventArgs e)
        {
            expressionList.Add("5");
            expressionString = String.Join("", expressionList);
            inputLabel.Text = expressionString;
        }

        private void button6_Click(object sender, EventArgs e)
        {
            expressionList.Add("6");
            expressionString = String.Join("", expressionList);
            inputLabel.Text = expressionString;
            
        }

        private void button7_Click(object sender, EventArgs e)
        {
            expressionList.Add("7");
            expressionString = String.Join("", expressionList);
            inputLabel.Text = expressionString;
        }

        private void button8_Click(object sender, EventArgs e)
        {
            expressionList.Add("8");
            expressionString = String.Join("", expressionList);
            inputLabel.Text = expressionString;
        }

        private void button9_Click(object sender, EventArgs e)
        {
            expressionList.Add("9");
            expressionString = String.Join("", expressionList);
            inputLabel.Text = expressionString;
        }

        private void button0_Click(object sender, EventArgs e)
        {
            expressionList.Add("0");
            expressionString = String.Join("", expressionList);
            inputLabel.Text = expressionString;
        }

        private void additionButton_Click(object sender, EventArgs e)
        {
            expressionList.Add("+");
            expressionString = String.Join("", expressionList);
            inputLabel.Text = expressionString;
        }

        private void subtractionButton_Click(object sender, EventArgs e)
        {
            expressionList.Add("-");
            expressionString = String.Join("", expressionList);
            inputLabel.Text = expressionString;
        }

        private void multiplicationButton_Click(object sender, EventArgs e)
        {
            expressionList.Add("*");
            expressionString = String.Join("",expressionList);
            inputLabel.Text = expressionString;
        }

        private void divisionButton_Click(object sender, EventArgs e)
        {
            expressionList.Add("/");
            expressionString = String.Join("", expressionList);
            inputLabel.Text = expressionString;
        }

        private void openParen_Click(object sender, EventArgs e)
        {
            expressionList.Add("(");
            expressionString = String.Join("", expressionList);
            inputLabel.Text = expressionString;
        }

        private void closeParen_Click(object sender, EventArgs e)
        {
            expressionList.Add(")");
            expressionString = String.Join("", expressionList);
            inputLabel.Text = expressionString;
        }
        private void powerButton_Click(object sender, EventArgs e)
        {
            expressionList.Add("^");
            expressionString = String.Join("", expressionList);
            inputLabel.Text = expressionString;
        }

        private void piButton_Click(object sender, EventArgs e)
        {
            expressionList.Add("pi");
            expressionString = String.Join("", expressionList);
            inputLabel.Text = expressionString;
        }

        private void equalButton_Click(object sender, EventArgs e)
        {
            Expression expression = new Expression(expressionString);
            double result = expression.calculate();

            outputLabel.Text = result.ToString();
        }

        private void clearButton_Click(object sender, EventArgs e)
        {
            if (expressionList.Count > 0) 
            {
                expressionList.RemoveAt(expressionList.Count - 1);
                expressionString = String.Join("", expressionList);
                inputLabel.Text = expressionString;
               
            }
            
        }

        private void allClearButton_Click(object sender, EventArgs e)
        {
            expressionList.Clear();
            expressionString = "";
            inputLabel.Text = expressionString;
            outputLabel.Text = "";
        }

        private void sinButton_Click(object sender, EventArgs e)
        {
            expressionList.Add($"{sinButton.Text}");
            expressionString = String.Join("", expressionList);
            inputLabel.Text = expressionString;
        }

        private void cosButton_Click(object sender, EventArgs e)
        {
            expressionList.Add($"{cosButton.Text}");
            expressionString = String.Join("", expressionList);
            inputLabel.Text = expressionString;
        }

        private void tan_Click(object sender, EventArgs e)
        {
            expressionList.Add($"{tanButton.Text}");
            expressionString = String.Join("", expressionList);
            inputLabel.Text = expressionString;
        }

        

        private void checkBox1_CheckedChanged(object sender, EventArgs e)
        {
            

            if (!alpha) 
            {
                shift = !shift;

                if (shift)
                {
                    sinButton.Text = "asin";
                    cosButton.Text = "acos";
                    tanButton.Text = "atan";
                }


                else
                {
                    sinButton.Text = "sin";
                    cosButton.Text = "cos";
                    tanButton.Text = "tan";
                }
            }

            else
            {
                shiftButton.Checked = false;
            }

            
        }

        private void alphaButton_CheckedChanged(object sender, EventArgs e)
        {

            if(!shift)
            {
                alpha = !alpha;

                if (alpha)
                {
                    sinButton.Text = "csc";
                    cosButton.Text = "sec";
                    tanButton.Text = "cot";
                }

                else
                {
                    sinButton.Text = "sin";
                    cosButton.Text = "cos";
                    tanButton.Text = "tan";

                }
            }

            else
            {
                inverseButton.Checked = false;
            }
            
        }

        private void button10_Click(object sender, EventArgs e)
        {
           Calculator calculator = new Calculator();
           calculator.Show();
        }
    }
}
