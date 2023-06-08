from flask import Flask, render_template, request
#from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    with open("Model_file/Gene_exp_individual_modality.pkl","rb") as f:
        Gene_exp_model = pickle.load(f)
    with open("Model_file/miRNA_exp_individual_modality.pkl","rb") as h:
        miRNA_exp_model = pickle.load(h)
    with open("Model_file/DNA_meth_individual_modality.pkl","rb") as i:
        DNA_Meth_model = pickle.load(i)
    with open("Model_file/Gene_exp_pls_individual_modality.pkl","rb") as j:
        Gene_exp_pls_model = pickle.load(j)
    with open("Model_file/miRNA_exp_PLS_individual_modality.pkl","rb") as k:
        miRNA_exp_pls_model = pickle.load(k)
    with open("Model_file/DNA_meth_pls_individual_modality.pkl","rb") as l:
        DNA_Meth_pls_model = pickle.load(l)
    with open("Model_file/Meta_model_with_Gene_miRNA_DNA_meth_without_pls.pkl","rb") as m:
        wo_pls = pickle.load(m)
    with open("Model_file/All_PLS.pkl","rb") as n:
        with_pls = pickle.load(n)
    with open("Model_file/Final_meta_model.pkl","rb") as o:
        final = pickle.load(o)

    if request.method == "POST":
        Gene_expression = request.files["Gene_expression"]
        miRNA_expression = request.files["miRNA_expression"]
        DNA_Meth = request.files["DNA_Meth"]

        df_gene_exp = pd.read_csv(Gene_expression,sep="\t")
        df_miRNA_exp = pd.read_csv(miRNA_expression,sep="\t")
        df_DNA_Meth = pd.read_csv(DNA_Meth,sep="\t")
        
        #Individual Modality
        pred_Gene = pd.DataFrame(Gene_exp_model.predict_proba(df_gene_exp[Gene_exp_model.feature_names_in_])[:,1],columns=["Gene_exp"])
        pred_miRNA = pd.DataFrame(miRNA_exp_model.predict_proba(df_miRNA_exp[miRNA_exp_model.feature_names_in_])[:,1], columns=["miRNA_exp"])
        pred_DNA_Meth = pd.DataFrame(DNA_Meth_model.predict_proba(df_DNA_Meth[DNA_Meth_model.feature_names_in_])[:,1],columns=["DNA_Meth"])
        # individual modality with PLS
        pred_Gene_PLS = pd.DataFrame(Gene_exp_pls_model.predict(df_gene_exp[Gene_exp_pls_model.feature_names_in_]),columns=["Gene_Exp_PLS_DA"])
        pred_miRNA_PLS = pd.DataFrame(miRNA_exp_pls_model.predict(df_miRNA_exp[miRNA_exp_pls_model.feature_names_in_]), columns=["miRNA_Exp_PLS_DA"])
        pred_DNA_Meth_PLS = pd.DataFrame(DNA_Meth_pls_model.predict(df_DNA_Meth[DNA_Meth_pls_model.feature_names_in_]),columns=["DNA_Meth_PLS_DA"])
        # meta model (1st layer)
        pred_wo_pls = pd.DataFrame(wo_pls.predict_proba(pd.concat([pred_Gene,pred_DNA_Meth,pred_miRNA],axis=1))[:,1], columns=["Gene_DNA_miRNA"])
        pred_w_pls = pd.DataFrame(with_pls.predict_proba(pd.concat([pred_Gene_PLS,pred_DNA_Meth_PLS,pred_miRNA_PLS],axis=1))[:,1], columns=["Gene_DNA_miRNA_PLS_DA"])
        # final meta model
        final_result = final.predict(pd.concat([pred_wo_pls,pred_w_pls,],axis=1))
        a = final_result.tolist()
        final_prediction = ["long survival" if x==1 else "short survival" for x in a ]
        final_op= zip(df_gene_exp.index.tolist(),final_prediction)

        
        return render_template("result.html", predictions=final_op)
    return render_template("home.html",gene_exp_feature_name = Gene_exp_model.feature_names_in_,
    miRNA_exp_feature_name = miRNA_exp_model.feature_names_in_,
    DNA_Meth_feature_name = DNA_Meth_model.feature_names_in_,
    Gene_exp_pls_feature_name = Gene_exp_pls_model.feature_names_in_,
    miRNA_exp_pls_feature_name = miRNA_exp_pls_model.feature_names_in_,
    DNA_Meth_pls_feature_name = DNA_Meth_pls_model.feature_names_in_
    )

if __name__ == "__main__":
    app.run(debug=True,port=8887)
