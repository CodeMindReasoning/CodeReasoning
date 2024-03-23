
<div align='center'>
<img src="https://github.com/CodeMindReasoning/CodeReasoning/blob/main/CodeMind-Logo.jpg" width="25%" height="25%" />
  <br>
</div>

Solely relying on test passing to evaluate Large Language Models (LLMs) for code synthesis may result in unfair assessment or promoting models with data leakage. As an alternative, we introduce CodeMind, a framework designed to gauge the code reasoning abilities of LLMs. CodeMind currently supports three code reasoning tasks: Independent Execution Reasoning (IER), Dependent Execution Reasoning (DER), and Specification Reasoning (SR). The first two evaluate models to predict the execution output of an arbitrary code or code the model could correctly synthesize. The third one evaluates the extent to which LLMs implement the specified expected behavior.

<!--### Paper
Interested to read more about CodeMind, the code reasoning tasks, and a grounded-theory study evaluating LLMs for code reasoning across five benchmarks and two programming languages? Please read the pre-print on Arxiv: https://arxiv.org/pdf/2402.09664.pdf-->

## CodeMind Framework

### Dependencies
Deployment and use of CodeMind require specific dependencies. Please check if all dependencies listed on ```requirements.txt``` are installed in your environment. 
To install all the dependencies, simply run the following command: ```pip install -r requirements.txt```

Need to register an OpenAI Key and write it into a local variable(```OPENAIKEY```)

### Dataset Structure
Please visit the ```/Dataset``` directory for the latest version of benchmarks integrated with CodeMins.

```
+---Avatar
|   |
|   +---Avatar-java
|   |
|   +---Avatar-python
|
+---CodeNet
|   |
|   +---CodeNet-java
|   |
|   +---CodeNet-python
|
+---CRUXEval
|
+---HumanEval
|
+---MBPP
```

### Using CodeMind
CodeMind currently supports three inductive code reasoning tasks: (1) Independent Execution Reasoning (IER), Dependent Execution Reasoning (DER), and Specification Reasoning (SR). Detailed instructions about using CodeMind to evaluate LLMs for these tasks are explained under each task's corresponding folder. 

### Results of the Grounded-Theory Study
You can find the raw results of our study under ```Results```. Please use CodeMind and try to reproduce our results!



### Prompt example for IER
<div align='center'>
<img src="https://github.com/CodeMindReasoning/CodeReasoning/blob/main/prompt-1.png" width="45%" height="25%" />
  <br>
</div>
Below is the prompt we used for GPT-3.5. Prompts for other models have very similar structure but are paired with some different special tokens.
```
<Instruction>
I want you to act as a Java code executor. I will give you a piece of Java code and its input. You need to think step by step and then print the output of code execution.
</Instruction>
Below is an example:
<Example>
Consider the following code:
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) {
        try {
            InputStreamReader isr = new InputStreamReader(System.in);
            BufferedReader br = new BufferedReader(isr);
            String strArr[] = br.readLine().split(" ");

            int n = Integer.parseInt(strArr[0]);
            int a = Integer.parseInt(strArr[1]);
            int b = Integer.parseInt(strArr[2]);
            int answer = 0;

            for (int i = 1; i < n + 1; i++) {
                int num = i;
                int sum = 0;

                while (num != 0) {
                        sum += num % 10;
                        num /= 10;
                }

                if (sum >= a && sum <= b ) {
                        answer = answer + i;
                }
            }
            System.out.println(answer);
            } catch (Exception e) {
            e.printStackTrace();
        }
    }

}
[Question]
What would be the output of code execution given the following input:
20 2 5
First analyze step by step about how the code processes the input to generate the output. 
Then print the output of the code based on your analysis.

Follow the following format:
<<<Analysis>>>
{YOUR ANALYSIS}
<<<Output>>>
{OUTPUT}
[END-OF-RESPONSE]

[Answer]
<<<Analysis>>>
The variable n, variable a and variable b are initialized with 20, 2 and 5 respectively according to the input. And variable sum is initialized with 0.
It enters a for loop and it iterates from 1 to 20 to check each integer i in this range. The value of variable i is also passed to variable num.
Inside the for loop, it calculates the sum of the digits of the current interger num by repeatedlly extracting the digits of number with a while loop and adding it to variable sum.
Then it checks if the calculated variable sum falls within the range [2, 5]. If it does, it adds the current interger i to variable answer. The condition is met when i is 2,3,4,5,11,12,13,14 and 20.
After the loop finishes, it print the fianl value of variable answer as output, which is 84.
<<<Output>>>
84
[END-OF-RESPONSE]
</Example>

`Consider the following code:
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException{

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String str = br.readLine();
		String ret = "";
		for (int i = 0; i < str.length(); i++) {
			char ch = str.charAt(str.length() - i - 1);
			ret += ch;
		}
		System.out.println(ret);
	}
}`

[Question]
What would be the output of code execution given the following input:
```w32nimda```
First analyze step by step about how the code processes the input to generate the output.
Then print the output of the code based on your analysis.
Follow the following format:
<<<Analysis>>>
{YOUR ANALYSIS}
<<<Output>>>
{OUTPUT}
[Answer]
```
