import pickle


f = open(r'/records/layer-4head-Transformer-100-hangzhou-0.0001/anon_4_4_hangzhou_real_5734.json_11_15_08_55_48/test_round/round_0/attention.pkl','rb')
data = pickle.load(f)
print(data)
