from recbole.quick_start import run_recbole

# run_recbole(model="LightGCN_Poly", dataset="TenRec", config_file_list=["config_tenrec.yaml"])

run_recbole(model="JGCF", dataset="gowalla", config_file_list=["configs/config_gowalla.yaml"]) 