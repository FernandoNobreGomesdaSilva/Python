@echo off
cd C:\Users\ferna\Drive\Area_de_Trabalho\Python\Estudo_Extracao_APIs
jupyter nbconvert --to notebook --execute Extracao_MySql.ipynb --output Extracao_MySql_EXECUTADO.ipynb
start jupyter lab
echo Extracao concluida.
pause


