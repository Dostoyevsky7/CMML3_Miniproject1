# CMML3_Miniproject1

This repository recorded 3 models with different hypothsis on AMPAR in LTP induction, which are the **Exocytosis model**, the **Receptor model** and the **Slot model**. The models are rule-based models using the Kappa language.

**Kasim** is used to run the models, which is available to be downloaded at https://kappalanguage.org. 

After setting up Kasim, the models can be run as follows:



```bash
bin\KaSim.exe Agents.ka Variables.ka Rules.ka Modification.ka Observables.ka 8020.ka -l 100 -o output.out
```

Where Agents.ka, Variables.ka, Rules.ka, Modification.ka, Observables.ka and 8020.ka are files constructing the model. The `Modification.ka` file can be adopted into different LTP protocols, including Theta Burst, compressed Theta Burst (cTheta Burst), spaced Theta Burst (sTheta Burst), High frequency stimulation (HFS) and weak LTP protocol.
