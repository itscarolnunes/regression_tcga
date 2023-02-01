import pandas as pd

df = pd.read_excel(".\data\clinical.xlsx")

df.columns

# selecionar somente as colunas que são interessantes para análise

df_s = df[['TARGET USI', 'Gender', 'Race', 'Ethnicity', 'Age at Diagnosis in Days', 'First Event', 'Event Free Survival Time in Days', 'Vital Status',
           'Overall Survival Time in Days', 'WBC at Diagnosis', 'Bone marrow leukemic blast percentage (%)', 'Peripheral blasts (%)', 'CNS disease']]


df2 = df_s.rename(columns={'TARGET USI': 'id', 'Age at Diagnosis in Days': 'idade_dias', 'First Event': 'primeiro_evento', 'Event Free Survival Time in Days': 'sobrevida_evento', 'Vital Status': 'status',
                  'Overall Survival Time in Days': 'sobrevida_global', 'WBC at Diagnosis': "leucocitos", 'Bone marrow leukemic blast percentage (%)': "blastos_mo", 'Peripheral blasts (%)': "blasto_sangue", 'CNS disease': "SNC"}, inplace=False)
df2.columns
# vendo se tem valores nulos
df2.isna().sum()

# temos valores nulos em 3 váriaveis vamos prencher os valores nulos com zeros
df2 = df2.fillna(0)

# algumas variaveis estão dispotas em dias, vamos transformar em anos para idade e meses para sobrevida

df2["idade"] = df2["idade_dias"].div(365).round()
df2["sobrevida_evento_meses"] = df2["sobrevida_evento"].div(30).round(2)
df2["sobrevida_global_meses"] = df2["sobrevida_global"].div(30).round(2)

df2.to_excel("clinical_selec.xlsx", index=False)
