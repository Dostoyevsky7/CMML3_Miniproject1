# CMML3_Miniproject1

This repository recorded 3 models with different hypothsis on AMPAR in LTP induction, which are the **Exocytosis model**, the **Receptor model** and the **Slot model**. The models are rule-based models using the Kappa language.


## 1. Kasim setup

**Kasim** is used to run the models, which is available to be downloaded at https://kappalanguage.org. 


## 2. Run the models
After setting up Kasim, the models can be run as follows:



```bash
bin\KaSim.exe Agents.ka Variables.ka Rules.ka Modification.ka Observables.ka 8020.ka -l 100 -o output.out
```

Where Agents.ka, Variables.ka, Rules.ka, Modification.ka, Observables.ka and 8020.ka are files constructing the model. The `Modification.ka` file can be adopted into different LTP protocols, including Theta Burst, compressed Theta Burst (cTheta Burst), spaced Theta Burst (sTheta Burst), High frequency stimulation (HFS) and weak LTP protocol.

Each protcol's modification files and time length used are as follows, which is the same in all 3 models:


### (1) Theta Burst protocol

```bash
bin\KaSim.exe Agents.ka Variables.ka Rules.ka theta_burst_modification.ka Observables.ka 8020.ka -l 120 -o output_Theta_Burst_60.out
```

### (2) compressed Theta Burst protocol

```bash
bin\KaSim.exe Agents.ka Variables.ka Rules.ka cTheta_burst_modification.ka Observables.ka 8020.ka -l 180 -o output_cTheta_60.out
```

### (3) spaced Theta Burst protocol

```bash
bin\KaSim.exe Agents.ka Variables.ka Rules.ka sTheta_burst_modification.ka Observables.ka 8020.ka -l 1500 -o output_sTheta_60.out
```

### (4) HFS protocol

```bash
bin\KaSim.exe Agents.ka Variables.ka Rules.ka HFS_modification.ka Observables.ka 8020.ka -l 120 -o output_HFS_60.out
```

### (5) weak LTP protocol

```bash
bin\KaSim.exe Agents.ka Variables.ka Rules.ka weak_LTP_modification.ka Observables.ka 8020.ka -l 600 -o output_sTheta_60.out
```

## 3. Visulization


The output of the Kasim is a `.out` file. Run the python script in each model's folder could plot visualization plots from the `.out` file:

```bash
python plot_kasim_single_output.py
```

Specifically, in the `plot_kasim_single_output.py`, the variable:


```python
input_file = "output_sTheta_60.out" 
```

could be changed into any of the `.out` files to get the results.

The variable:
```python
label = "sTheta_60" 
```
would create a folder named "plots_sTheta_60", this variable could also be changed into any names wanted.

The output of the script would be focus on variables including:
```python
input_vars = [
    "Calcium_Levels",
    "Glutamate_level",
    "CaGlu",
    "Glu_Trigger",
]

mechanism_vars = [
    "Active_CaM",
    "PP2B",
    "cAMP_levels",
    "PKA_a",
    "Phos_CK_subunits",
    "CaMKII_CaM",
    "actPKC_level",
]

phenotype_vars = [
    "Synaptic_receptors",
    "AMPA_membrane",
    "AMPA_PSD",
    "Conductance_S845_measure",
    "Conductance_S831_measure",
    "S845_P",
    "S845_PP",
    "S831_P",
    "S831_PP",
]
```
