"""Taller evaluable"""


import glob
import pandas as pd


def load_input(input_directory):

    filenames = glob.glob(f"{input_directory}\*.txt")
    # dataframes=[]
    # for filename in filenames:
    #     dataframes.append(pd.read_csv(filenames[0], sep="\t", header=None, names=["text"]))

    dataframes = [
        pd.read_csv(filename, sep="\t", header=None, names=["text"])
        for filename in filenames
    ]
    concatenated_df = pd.concat(dataframes, ignore_index=True)
    return concatenated_df

    """Load text files in 'input_directory/'"""


# Lea los archivos de texto en la carpeta input/ y almacene el contenido en
# un DataFrame de Pandas. Cada línea del archivo de texto debe ser una
# entrada en el DataFrame.
#


def clean_text(dataframe):
    dataframe = dataframe.copy()
    dataframe["text"] = dataframe["text"].str.lower()
    dataframe["text"] = dataframe["text"].str.replace(".", "")
    dataframe["text"] = dataframe["text"].str.replace(",", "")
    return dataframe
    """Text cleaning"""
    #
    # Elimine la puntuación y convierta el texto a minúsculas.
    #


def count_words(dataframe):
    dataframe = dataframe.copy()
    dataframe["text"] = dataframe["text"].str.split()
    dataframe = dataframe.explode("text")
    dataframe["count"] = 1
    dataframe = dataframe.groupby("text").agg({"count": "sum"})
    """Word count"""
    return dataframe


def count_words_(dataframe):
    dataframe = dataframe.copy()
    dataframe["text"] = dataframe["text"].str.split()
    dataframe = dataframe.explode("text")
    dataframe = dataframe["text"].value_counts()
    """Word count"""
    return dataframe


def save_output(dataframe, output_filename):
    dataframe.to_csv(output_filename, sep="\t", index=True, header=False)
    """Save output to a file."""


#
# Escriba la función job, la cual orquesta las funciones anteriores.
#
def run(input_directory, output_filename):
    df = load_input(input_directory)
    df = clean_text(df)
    df = count_words_(df)
    save_output(df, output_filename)
    """Call all functions."""


if __name__ == "__main__":
    run(
        "input",
        "output.txt",
    )
