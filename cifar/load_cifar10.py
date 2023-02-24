import numpy as np
import os
import pickle

def unpickle(file):
    with open(file,'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict

# 创建训练样本和测试样本
def CreatData():
    """
    返回训练集和测试集,以及对应标签
    格式为numpy.ndarray格式

    """
    # 创建训练样本
    # 依次加载batch_data_i,并合并到x,y
    x = []
    y = []
    for i in range(1, 6):
        # 以下地址按照实际数据集存放路径自行修改
        batch_path = './cifar-10-python/cifar-10-batches-py/' + f'data_batch_{i}'

        batch_dict = unpickle(batch_path)
        train_batch = batch_dict[b'data'].astype('float')
        train_labels = np.array(batch_dict[b'labels'])
        x.append(train_batch)
        y.append(train_labels)
    # 将5个训练样本batch合并为50000x3072，标签合并为50000x1
    # np.concatenate默认axis=0，为纵向连接
    traindata = np.concatenate(x)
    trainlabels = np.concatenate(y)

    # 创建测试样本
    # 直接写cifar-10-batches-py\test_batch会报错，因此把/t当作制表符了，应用\\;
    #    test_dict=unpickle("cifar-10-batches-py\\test_batch")

    # 建议使用os.path.join()函数
    # 以下地址按照实际数据集存放路径自行修改
    testpath = os.path.join('./cifar-10-python/cifar-10-batches-py', 'test_batch')
    
    test_dict = unpickle(testpath)
    testdata = test_dict[b'data'].astype('float')
    testlabels = np.array(test_dict[b'labels'])

    return traindata, trainlabels, testdata, testlabels
