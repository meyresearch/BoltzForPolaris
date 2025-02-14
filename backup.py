# def create_fasta_file(df, dir_name):
#     os.makedirs(dir_name, exist_ok=True)
#     for i, row in df.iterrows():
  
#         chain_a = row['Chain A Sequence']
#         chain_b = row['Chain B Sequence']
#         chain_cx = row['CXSMILES']
       
#         with open(f"{dir_name}/seq_{i}.fasta", "w") as f:
#             f.write(f">A|protein|\n{chain_a}\n")
#             f.write(f">B|protein|\n{chain_b}\n")
#             f.write(f">E|smiles\n{chain_cx}\n")
            
# create_fasta_file(df, "train_fasta")


# # for all chain A,B,CX SMILES create the fasta file in a dir
# import os


# def create_fasta_file(df, dir_name):
#     os.makedirs(dir_name, exist_ok=True)
#     for i, row in df.iterrows():
#         if i == 20:
#             break
#         chain_a = row['Chain A Sequence']
#         chain_b = row['Chain B Sequence']
#         chain_cx = row['CXSMILES']
       
#         with open(f"{dir_name}/seq_{i}.fasta", "w") as f:
#             f.write(f">A|protein|\n{chain_a}\n")
#             f.write(f">B|protein|\n{chain_b}\n")
#             f.write(f">E|smiles\n{chain_cx}\n")
            
# create_fasta_file(df, "train_fasta")


# with fsspec.open("ligand_poses_reference_structures.zip") as fd:
#     with zipfile.ZipFile(fd, 'r') as zip_ref:
#         zip_ref.extractall("./reference_structures/")




# with TemporaryDirectory() as tmpdir: 

#     tmpdir = Path(tmpdir)
    
#     # The RDKit Mol object supports various IO formats. 
#     # Here we use the Datamol library (which wraps RDKit) to effortlessly write to SDF
#     # dm.to_sdf(datapoint["Ligand Pose"], tmpdir / "mol.sdf")

#     # Similarly, the Biotite AtomArray also support various IO formats
#     # Here we use fastpdb, a fast drop-in replacement for Biotite IO.
#     out_file = fastpdb.PDBFile()
#     out_file.set_structure(datapoint["Complex Structure"])
#     out_file.write(tmpdir / "complex.pdb")


# # total_sample = 20

# for i in range(100):
#     # I want to save datapoints in reference as pdb
#     datapoint = competition[i]['Complex Structure']
    
#     out_file = fastpdb.PDBFile()
#     out_file.set_structure(datapoint)
#     out_file.write(reference / f"complex_{i}.pdb")
   
    