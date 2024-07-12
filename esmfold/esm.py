import streamlit as st
import requests
import urllib3
import py3Dmol

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
url = "https://api.esmatlas.com/foldSequence/v1/pdb/"

def get_pdb(sequence):
    response = requests.post(
        url,
        data=sequence,
        verify=False 
    )
    return response.text

def read_fasta(file):
    sequence = ""
    for line in file:
        line = line.decode("utf-8").strip()
        if line.startswith(">"):
            continue
        sequence += line
    return sequence

def visualize_pdb(pdb_data):
    view = py3Dmol.view(width=800, height=800)
    view.addModel(pdb_data, 'pdb')
    view.setStyle({'cartoon': {'color': 'spectrum'}})
    view.spin()
    view.zoomTo()
    return view

st.set_page_config(page_title='ESMFold Protein Structure Predictor', page_icon='🎈')

st.sidebar.title('🎈 ESMFold')
st.sidebar.write('[*ESMFold*](https://esmatlas.com/about) is an end-to-end single sequence protein structure predictor based on the ESM-2 language model. For more information, read the [research article](https://www.biorxiv.org/content/10.1101/2022.07.20.500902v2) and the [news article](https://www.nature.com/articles/d41586-022-03539-1) published in *Nature*.')
st.sidebar.subheader('Protein Sequence Format')
st.sidebar.write("""
The protein sequence should be provided as a string of amino acid residues using the standard one-letter amino acid codes.
- A = Alanine
- C = Cysteine
- D = Aspartic acid
- E = Glutamic acid
- F = Phenylalanine
- G = Glycine
- H = Histidine
- I = Isoleucine
- K = Lysine
- L = Leucine
- M = Methionine
- N = Asparagine
- P = Proline
- Q = Glutamine
- R = Arginine
- S = Serine
- T = Threonine
- V = Valine
- W = Tryptophan
- Y = Tyrosine
""")
input_sequence = st.sidebar.text_area("Protein Sequence", height=200)
uploaded_file = st.sidebar.file_uploader("Upload FASTA file", type=["fasta", "fa"])

if st.sidebar.button("Predict Structure"):
    if input_sequence or uploaded_file:
        st.sidebar.write("Getting your structure...")

        if uploaded_file:
            input_sequence = read_fasta(uploaded_file)
        
        pdb_data = get_pdb(input_sequence)
        
        st.sidebar.download_button(
            label="Download PDB File",
            data=pdb_data,
            file_name="predicted_structure.pdb",
            mime="chemical/x-pdb"
        )
     
        st.subheader("3D Visualization of the Predicted Protein Structure")
        view = visualize_pdb(pdb_data)
        view_html = view._make_html()
        st.components.v1.html(view_html, width=800, height=800)
        
    else:
        st.sidebar.error("Please enter a protein sequence or upload a FASTA file.")
