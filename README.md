# Fuzzy Logic-based Ranking System for Car Workshops in Bandung

This project aims to build a Fuzzy Logic-based system to select the top 10 car workshops in Bandung city, using a dataset provided in the file "bengkel.xlsx". The dataset consists of 100 car workshops with two attributes: Service Quality (real number 1-100; higher values indicate better quality) and Price (real number 1-10; higher values indicate higher prices). The system reads the input file "bengkel.xlsx" and generates an output file "peringkat.xlsx" containing the rankings of the top 10 car workshops along with their scores (output Defuzzification).

## Design and Analysis

The following aspects already designed and analyzed:

1. Number and Linguistic Names of Input Attributes: Determine the number of linguistic terms and their names for each input attribute, i.e., Service Quality and Price.

2. Shape and Range of Input Membership Functions: Define the shape and range of the membership functions for each linguistic term of the input attributes.

3. Inference Rules: Establish the inference rules that connect the input attributes to the output, specifying the relationship between the linguistic terms.

4. Defuzzification Method: Choose a defuzzification method to convert the fuzzy output into a crisp value. Determine the shape and range of the output membership functions accordingly.

## Implementation

The following processes already implemented in the program:

1. Data Reading: Read the data from the input file.

2. Fuzzification: Apply fuzzification to convert the crisp input values into fuzzy sets using the defined membership functions.

3. Inference: Perform inference based on the predefined rules to determine the fuzzy output.

4. Defuzzification: Apply a defuzzification method to obtain a crisp value from the fuzzy output.

5. Output Saving: Save the output, including the rankings of the top 10 car workshops along with their scores, to the output file "peringkat.xlsx".

The program should be implemented without using any external libraries, building each step from scratch.

## Output

The program will generate an output file "peringkat.xlsx" that contains the rankings of the top 10 car workshops in Bandung along with their scores (output Defuzzification). The rankings will be based on the fuzzy logic calculations and will provide a crisp representation of the workshop's quality and price factors.

## Contact

If you have any questions or suggestions regarding this project, please feel free to contact me. You can reach me at [aryafikriansyah@gmail.com].
