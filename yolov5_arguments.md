##--weights
**选择预训练权重模型，若default为空则用程序自带初始权重**  
parser.add_argument('--weights', type=str, default=ROOT / 'yolov5s.pt', help='initial weights path')
*default='权重文件的路径地址'*

##--cfg
**选择神经网络模型，default为' '时使用程序自带模型**  
parser.add_argument('--cfg', type=str, default='yolov5s.yaml', help='model.yaml path')
*default='模型yaml文件的路径地址'*

##--data
**样本数据路径，进入到mydata.yaml文件里修改修改**  
parser.add_argument('--data', type=str, default=ROOT / 'data/mydata.yaml', help='dataset.yaml path')
*default='数据yaml文件的路径地址'*

##--hyp
**超参数：动量、衰减率、box设置等等，一般情况下用不到**  
parser.add_argument('--hyp', type=str, default=ROOT / 'data/hyps/hyp.scratch.yaml', help='hyperparameters path')  
*hyp.scratch.yaml文件中包含调参数据*  

##--epochs
**训练的轮数：训练几轮，设定epoch数量。源码中 default 值为 300，训练轮次则显示为 0~299**  
parser.add_argument('--epochs', type=int, default=400)  

##--batch-size
**每次网路输入的数据量：每批次的输入数据量，default=-1时自动调节大小**  
parser.add_argument('--batch-size', type=int, default=32, help='total batch size for all GPUs, -1 for autobatch')  

##--imgsz
**图片大小：训练集和测试集图片的像素大小，输入默认640*640**  
parser.add_argument('--imgsz', '--img', '--img-size', type=int, default=640, help='train, val image size (pixels)')

##--rect
**设置矩阵的训练方式：作用是减去一些不必要信息，加速模型推理过程。默认为False**

##--resume
**是否在最近训练的一个模型基础上继续训练：default 值默认是 false，当想要 default 为 true 时必须指定在哪个模型上继续训练。指定的模型路径按字符串形式赋值给 default。**  
parser.add_argument('--resume', nargs='?', const=True, default=False, help='resume most recent training')

##--nosave
**只保存最后一次 pt 文件**  
parser.add_argument('--nosave', action='store_true', help='only save final checkpoint')

##--notest
**生效后只在最后一次进行测试**  
parser.add_argument('--noval', action='store_true', help='only validate final epoch')

##--noautoanchor
**用于设置在目标检测任务中是否采用锚点 / 锚框。**  
**遍历输入图像上所有可能的像素框，然后选出正确的目标框，并对位置和大小进行调整就可以完成目标检测任务。**  
**默认开启，用这种方式来简化模型训练过程。**  
parser.add_argument('--noautoanchor',action='store_true', help='disable autoanchor check')

##--evolve
**对x代超参数进行优化**
**作用是寻找最优超参数的方式，方法是利用遗传算法自动搜索超参数。默认不开启**

##--bucket
**这个参数是 yolov5 作者将一些东西放在谷歌云盘，可以进行下载。**
parser.add_argument('--bucket', type=str, default='', help='gsutil bucket')

##--cache
**生效后将对图片进行缓存，以便更好地进行训练**
parser.add_argument('--cache', type=str, nargs='?', const='ram', help='--cache images in "ram" (default) or "disk"')

##--image-weights
**生效后对于那些训练不好的图片，会在下一轮中增加一些权重。**
parser.add_argument('--image-weights', action='store_true', help='use weighted image selection for training')

##--device
**用于设置运行 pytorch 框架的使用设备，是用 GPU cuda，还是 cpu**
parser.add_argument('--device', default='', help='cuda device, i.e. 0 or 0,1,2,3 or cpu')

##--multi-scale
**对图片尺度进行变换**
parser.add_argument('--multi-scale', action='store_true', help='vary img-size +/- 50%%')

##--single-cls
**用于设定训练数据集是单类别还是多类别。默认为 false，意味着是多类别。**
parser.add_argument('--single-cls', action='store_true', help='train multi-class data as single-class')

##--adam
**优化器：填入到 Edit Configuration --> Parameters 中即为 true ，意味着要用此优化器；否则为 false，为 false 时用的是随机梯度下降（SGD）优化算法。**
parser.add_argument('--adam', action='store_true', help='use torch.optim.Adam() optimizer')

##--sync-bn
**进行多 GPU 进行分布式训练**
parser.add_argument('--sync-bn', action='store_true', help='use SyncBatchNorm, only available in DDP mode')

##--workers
**多线程：这里建议 default 设置为 0。**
parser.add_argument('--workers', type=int, default=0, help='max dataloader workers (per RANK in DDP mode)')


##--project
**用于指定训练好的模型的保存路径**
parser.add_argument('--project', default=ROOT / 'runs/train', help='save to project/name')

##--name
**用于设定保存的模型文件名**
parser.add_argument('--name', default='exp', help='save to project/name')

##--exist-ok
**用于设定预测结果的保存存在位置情况。当激活时为true，在name指定文件夹下保存，源码中保存在exp文件夹下；当不激活时为false，在新命名的文件夹下保存**
parser.add_argument('--exist-ok', action='store_true', help='existing project/name ok, do not increment')

##--quad
**解释为 quad 数据加载的相关设置。**
**简单理解，生效后可以在比前面 “–img-size” 部分设置的训练测试数据集更大的数据集上训练。**
parser.add_argument('--quad', action='store_true', help='quad dataloader')
* 好处是在比默认 640 大的数据集上训练效果更好
* 副作用是在 640 大小的数据集上训练效果可能会差一些

##--linear-lr
**用于对学习速率进行调整。默认为 false，含义是通过余弦函数来降低学习率。**
parser.add_argument('--linear-lr', action='store_true', help='linear LR')

##--label-smoothing
**用于对标签进行平滑处理。作用是防止在分类算法中过拟合情况的产生。**
parser.add_argument('--label-smoothing', type=float, default=0.0, help='Label smoothing epsilon')

##--patience
**提前结束：若epoch没有提升则提前结束**
parser.add_argument('--patience', type=int, default=100, help='EarlyStopping patience (epochs without improvement)')

##--freeze
**冻结层：可适当减少冻结层数**
parser.add_argument('--freeze', type=int, default=24, help='Number of layers to freeze. backbone=10, all=24')

##--save-period
**用于记录训练日志信息，int 型，默认为 -1**
parser.add_argument('--save-period', type=int, default=-1, help='Save checkpoint every x epochs (disabled if < 1)')

##--local_rank
**DistributedDataParallel 单机多卡训练，一般不改动**
parser.add_argument('--local_rank', type=int, default=-1, help='DDP parameter, do not modify')

##--entity
**与 wandb 库相关的参数设置**
parser.add_argument('--entity', default=None, help='W&B: Entity')

##--upload_dataset
**wandb 库对应的东西**
parser.add_argument('--upload_dataset', action='store_true', help='W&B: Upload dataset as artifact table')

##--bbox_interval
**与 wandb 库相关的参数设置**
parser.add_argument('--bbox_interval', type=int, default=-1, help='W&B: Set bounding-box image logging interval')

##--artifact_alias
**与 wandb 库相关的参数设置**
parser.add_argument('--artifact_alias', type=str, default='latest', help='W&B: Version of dataset artifact to use')










