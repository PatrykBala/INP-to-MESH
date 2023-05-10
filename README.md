# Mesh generator for Abaqus.
![image](https://user-images.githubusercontent.com/73967948/174500377-8e004cc4-9d14-4db3-a0a3-90624fbe6be8.png)

## General info
Script that creates an input file for the Abaqus program (inp format) containing a finite element mesh generated on a two-dimensional rectangular element. The user enters the name of the element as input, the height and width of the element, as well as the number of mesh vertices at the edges of the element. Data can be entered using, for example, a json or xml file, which is then loaded by the script. The script can run independently of the Abaqus application. 

<sub> PL: Skrypt, który tworzy plik wejściowy dla programu Abaqus (format inp) zawierający siatkę elementów skończonych wygenerowaną na dwuwymiarowym elemencie prostokątnym. Użytkownik jako dane wejściowe wprowadza nazwę elementu, wysokość i szerokość elementu, a także ilość wierzchołków siatki na krawędziach elementu. Dane mogą być wprowadzane używając np. pliku json lub xml, który następnie jest wczytywany przez skrypt. Skrypt może działać niezależnie od aplikacji Abaqus. </sub>

## Technologies
Python.

## Setup
1. **Extract** the archive.
2. Due to the ease of pointing to the path in *Abaqus*, **place** the extracted folder from the archive in *C:/temp*.
3. **Start** your integrated development environment, for exaple *PyCharm*.
4. **Enter** the data in the *input.json* file.<br>
![image](https://github.com/PatrykBala/INP-to-MESH/assets/73967948/2c14b95b-8cf8-456a-af46-8dde1b060441)<br>
&emsp;*name* - this will be the name of the file
&emsp;*width, height* - dimensions
&emsp;*nodes_count* - the number of nodes on the edges
5. **Point** to the extracted folder (in your development environment).<br>
![image](https://github.com/PatrykBala/INP-to-MESH/assets/73967948/0753310f-5f65-45c2-b259-8e49f8b9d337)<br>
6. **Run** the script.<br>
![image](https://github.com/PatrykBala/INP-to-MESH/assets/73967948/7e610885-d492-4896-a192-69d809c68619)<br>
7. Additional files will appear in the folder you extracted at the beginning.<br>
![image](https://github.com/PatrykBala/INP-to-MESH/assets/73967948/8ce62fc1-2dd1-450a-9217-eb625135a0bb)<br>
8. The file with the expansion .inp is the input file for the *Abaqus* program.
9. **Run** the *Abaqus* program and **import** the input file, pointing to its location.<br>
![image](https://github.com/PatrykBala/INP-to-MESH/assets/73967948/340e53a8-7e29-4bae-993c-27f27854b923)<br>
11. **Select** the model.<br>
![image](https://github.com/PatrykBala/INP-to-MESH/assets/73967948/8d519981-31a9-4a00-92b0-50e1e359592f)<br>
<br>
A generated element containing the finite element mesh will appear on the workspace.<br>
After running the script in the IDE, a .png file with known dimensions and nodes will appear in the extracted folder.
