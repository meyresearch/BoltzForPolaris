## It is a work in progress. I will update it as I progress through the challenge.

The main file is the pred_test.ipynb where I play around.
run.py is the script that I use to run the model on remote compute.


-> pred_test.ipynb is the main file where I play around with the data and the model.
-> reference_structures contain reference complex pdb to which I align my test data.
-> reference_complex contain complexes to which train data is aligned.
-> test_ligand_bond_fixed contains my prediction data with their bond fixed with my updated script to transfer bond knowledge
-> train_ligand_bond_fixed contains boltz-1 prediction for first 100 molecules in the train data. The labelling is offset by 1 compared to the original data, because the first molecule is not right, need look into this. But everything else is fine, so its about 99 molecules.
