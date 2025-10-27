import SimpleITK as sitk
import matplotlib.pyplot as plt

case_path= r'/Data/CAMUS/CAMUS/testing/patient0001/patient0001_4CH_sequence.mhd'  #图像路径

itkimage=sitk.ReadImage(case_path)

print(itkimage)   #这部分给出了关于图像的信息,可以打印处理查看

image=sitk.GetArrayFromImage(itkimage)

plt.figure(1)
plt.imshow(image[1,:,:])  #查看第1张图像
plt.show()
