import os
import xml.etree.ElementTree as ET
import re

# Definisci i valori dei parametri CTT e NUM
start_value = 300
end_value = 2550
step = 250

CTT_list = [str(value) for value in range(start_value, end_value + 1, step)]
#CTT_list = [str(3000)]

dockerUp = "docker-compose up -d"
dockerDown = "docker-compose down"

for CTT in CTT_list: 
    for NUM in range(1,4):

        # Caricamento documento XML
        tree = ET.parse("testPlan.jmx")
        root = tree.getroot()

        # Trova l'elemento desiderato nel documento XML
        for collector in root.iter("ResultCollector"):
            testname = collector.get("testname")
            
            # Modifica il testname con i valori dei parametri
            collector.set("testname", f"{CTT}r_{str(NUM)}_dk.csv")

        # Salva le modifiche nel file XML
        tree.write("testPlan.jmx")

        for string_prop in root.iter("stringProp"):
            name = string_prop.get("name")
            if name == "filename":
                # Modifica il valore dell'elemento con i valori dei parametri
                string_prop.text = f"/Users/carloportosalvo/Desktop/Università/Impianti/results/{CTT}_{str(NUM)}_dk.csv"

        # Salva le modifiche nel file XML
        tree.write("testPlan.jmx")

        for constant_timer in root.iter("ConstantThroughputTimer"):
            value_element = constant_timer.find(".//value")
            if value_element is not None:
                value_element.text = CTT

        # Salva le modifiche nel file XML
        tree.write("testPlan.jmx")

        file_path = './Ex1/entrypoint.sh'

        # Costruisci il nuovo valore di FILENAME
        new_filename = f"results/{CTT}_{NUM}_dk.csv"

        # Leggi il contenuto del file entrypoint.sh
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Cerca la riga in cui è definito FILENAME e sostituiscila con il nuovo valore
        for i, line in enumerate(lines):
            if line.startswith('FILENAME='):
                lines[i] = f'FILENAME="{new_filename}"\n'

        # Scrivi il nuovo contenuto nel file
        with open(file_path, 'w') as file:
            file.writelines(lines)

        os.system(dockerUp)
        os.system("sleep 5")
        os.system(f"./apache-jmeter-5.6.2/bin/jmeter.sh -n -t testPlan.jmx -l ./results/{CTT}r_{str(NUM)}_dk.csv -e -o ./results/{CTT}r_{str(NUM)}_dk-report -Jjmeter.save.saveservice.output_format=csv")
        os.system(dockerDown)
        os.system("docker rmi impianti-server")
