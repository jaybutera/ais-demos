HOW TO SET UP

## For ClarifAI
```python
sudo pip install clarifai
```

## For Conda
1. Install Python
2. Install pip
3. Add Python and pip to your PATH if you haven’t
4. Install Miniconda3:
 - wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
 - ./Miniconda3-latest-Linux-x86_64.sh
5. Clone repository
 - git clone https://github.com/jaybutera/ais-demos.git
6. Copy environment.yml from git repo to Miniconda3 directory
 - Overwrite existing environment.yml file
7. Create Miniconda3 environment:
 - conda env create -f environment.yml
8. Activate your environment
 - source activate dnn
9. Run the code
 - python <FILENAME>
