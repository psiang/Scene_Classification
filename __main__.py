from rsidea.model import *
import os
import tensorflow as tf
from rsidea.util.history import *
from rsidea.util.draw import *
import matplotlib.image as mpimg
from rsidea.preprocess import read_data, read_label, split_data

save = True

"""googlenet demo"""
# 读取数据
x, y = read_data.read_SIRI_WHU()
# 分割数据
x_train, y_train, x_test, y_test = split_data.split(x, y)
# 获取未训练模型
model = GoogLeNet(input_shape=x_train[0].shape, output_shape=12)
# 配置模型
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
# 填入数据进行训练并保存模型
history = model.fit(x_train, y_train, epochs=5,
                    validation_data=(x_test, y_test))
history = history.history
# 模型保存
if save:
    model.save(".\\model_data\\model\\googlenet_SIRI_WHU.h5")
    model.save_weights(".\\model_data\\weight\\googlenet_SIRI_WHU.h5")
    save_history(history, ".\\model_data\\history\\googlenet_SIRI_WHU.json")
    print("Saved!")
# # 模型评测
# model.evaluate(x_test, y_test, verbose=2)
# 画图
draw_accuracy(history)
draw_loss(history)
# 单张预测
names = read_label.read_SIRI_WHU()
img = mpimg.imread(".\\data\\demo.jpg") / 255.0  # 读取图像数据
draw_predict_demo(model, img, names)
