'''
This a pytorch series, so torch functionalities are been used, all of these operations can also be performed with numpy and tensorflow as well.
'''

import torch

device = "cuda" if torch.cuda.is_available() else 'cpu'

########    Tensor Initialization   ###############

my_tensor = torch.tensor([[1,2,3],[4,5,6],[7,8,9]])

print("original tensor:",my_tensor)
print("Size of tensor",my_tensor.size())

############################################################

# Comman Initilization Techniques

############################################################

print("Empty matrix:",torch.empty(size = (3,3)))
print("Null matrix:",torch.zeros(size = (3,3)))
print("Random matrix:",torch.rand(size = (3,3)))
print("Identity matrix:",torch.eye(3,3))
print(torch.arange(11))
print("Diagonal Matrix",torch.diag(torch.rand(3)))

############################################################

## Convert Tensors to other data types

############################################################

print('Boolean Converted :',my_tensor.bool())
print('int16 Converted :',my_tensor.short())
print('int64 Converted :',my_tensor.long())
print('float16 Converted :',my_tensor.half())
print('float32 Converted :',my_tensor.float())
print('float64 Converted :',my_tensor.double())

############################################################

# Array to Tensor conversion and vice-versa

###########################################################
import numpy as np

arr = np.zeros((5,5))
tensor = torch.from_numpy(arr)

print("Original Array ",arr)
print("Converted Tensor",tensor)

converted_array = tensor.numpy()
print("Converted Array",converted_array)

############################################################

## Tensor Math Operatins

############################################################

x = torch.tensor([1,2,3])
y = torch.tensor([4,5,6])

## Addition
z_add = torch.empty(3)
torch.add(x,y,out=z_add)      #1.
z2_add = torch.add(x,y)        #2.
z_add_ = x + y                  #3. 

## Subtraction
z_sub = torch.empty(3)
torch.sub(x,y,out=z_sub)      #1.
z2_sub = torch.sub(x,y)        #2.
z_sub_ = x - y                  #3. 

## Division
z_div = torch.empty(3)
torch.div(x,y,out=z_div)      #1.
z2_div = torch.div(x,y)        #2.
z_div_ = x / y                  #3. 

##  Multiplication
z_mul = torch.empty(3)
torch.mul(x,y,out=z_mul)      #1.
z2_mul = torch.mul(x,y)        #2.
z_mul_ = x * y                  #3. 


# -- Inplace Operations --
t = torch.zeros(3)

t.add_(x)  # Whenever we have operation followed by _ it will mutate the tensor in place
t += x  # Also inplace: t = t + x is not inplace, bit confusing.

# -- Exponentiation (Element wise if vector or matrices) --
z_exp = x.pow(2)  # z = [1, 4, 9]       1.
z_exp = x ** 2  # z = [1, 4, 9]         2.

# -- Matrix Multiplication --
x1 = torch.rand((2, 5))
x2 = torch.rand((5, 3))
x3 = torch.mm(x1, x2)  # Matrix multiplication of x1 and x2, out shape: 2x3
x3 = x1.mm(x2)  # Similar as line above

# -- Matrix Exponentiation --
matrix_exp = torch.rand(5, 5)
# print(matrix_exp.matrix_power(3))     # is same as matrix_exp (mm) matrix_exp (mm) matrix_exp

# -- Element wise Multiplication --
z_ele_mul = x * y  # z = [9, 16, 21] = [1*9, 2*8, 3*7]

# -- Dot product --
z_dot = torch.dot(x, y)  # Dot product, in this case z = 1*9 + 2*8 + 3*7

# -- Batch Matrix Multiplication --
batch = 32
n = 10
m = 20
p = 30
tensor1 = torch.rand((batch, n, m))
tensor2 = torch.rand((batch, m, p))
out_bmm = torch.bmm(tensor1, tensor2)  # Will be shape: (b x n x p)

# -- Example of broadcasting --
x1 = torch.rand((5, 5))
x2 = torch.ones((1, 5))

z = (x1 - x2)  # Shape of z is 5x5: How? The 1x5 vector (x2) is subtracted for each row in the 5x5 (x1)
z = (x1 ** x2)  # Shape of z is 5x5: How? Broadcasting! Element wise exponentiation for every row

# Other useful tensor operations
sum_x = torch.sum(x, dim=0)  # Sum of x across dim=0 (which is the only dim in our case), sum_x = 6

values, indices = torch.max(x, dim=0)  # Can also do x.max(dim=0)
values, indices = torch.min(x, dim=0)  # Can also do x.min(dim=0)
abs_x = torch.abs(x)  # Returns x where abs function has been applied to every element
z_argmax = torch.argmax(x, dim=0)  # Gets index of the maximum value
z_argmin = torch.argmin(x, dim=0)  # Gets index of the minimum value
mean_x = torch.mean(x.float(), dim=0)  # mean requires x to be float
z = torch.eq(x, y)  # Element wise comparison, in this case z = [False, False, False]
sorted_y, indices = torch.sort(y, dim=0, descending=False)

z = torch.clamp(x, min=0)
# All values < 0 set to 0 and values > 0 unchanged (this is exactly ReLU function)
# If you want to values over max_val to be clamped, do torch.clamp(x, min=min_val, max=max_val)

x = torch.tensor([1, 0, 1, 1, 1], dtype=torch.bool)  # True/False values
z = torch.any(x)  # will return True, can also do x.any() instead of torch.any(x)
z = torch.all(x)  # will return False (since not all are True), can also do x.all() instead of torch.all()

# ============================================================= #
#                        Tensor Indexing                        #
# ============================================================= #

batch_size = 10
features = 25
x = torch.rand((batch_size, features))

# Get first examples features
print(x[0].shape)  # shape [25], this is same as doing x[0,:]

# Get the first feature for all examples
print(x[:, 0].shape)  # shape [10]

# For example: Want to access third example in the batch and the first ten features
print(x[2, 0:10].shape)  # shape: [10]

# For example we can use this to, assign certain elements
x[0, 0] = 100

# Fancy Indexing
x = torch.arange(10)
indices = [2, 5, 8]
print(x[indices])  # x[indices] = [2, 5, 8]

x = torch.rand((3, 5))
rows = torch.tensor([1, 0])
cols = torch.tensor([4, 0])
print(x[rows, cols])  # Gets second row fifth column and first row first column

# More advanced indexing
x = torch.arange(10)
print(x[(x < 2) | (x > 8)])  # will be [0, 1, 9]
print(x[x.remainder(2) == 0])  # will be [0, 2, 4, 6, 8]

# Useful operations for indexing
print(torch.where(x > 5, x, x * 2))  # gives [0, 2, 4, 6, 8, 10, 6, 7, 8, 9], all values x > 5 yield x, else x*2

x = torch.tensor([0, 0, 1, 2, 2, 3, 4]).unique()  # x = [0, 1, 2, 3, 4]
# print(x.ndimension())  # The number of dimensions, in this case 1. if x.shape is 5x5x5 ndim would be 3

x = torch.arange(10)
# print(x.numel())  # The number of elements in x (in this case it's trivial because it's just a vector)


# ============================================================= #
#                        Tensor Reshaping                       #
# ============================================================= #

x_new = torch.arange(9)

x_3x3 = x_new.view(3, 3)
     # is the same as   
x_3x3 = x_new.reshape(3, 3)

y_cont = x_3x3.t()
print(y_cont.is_contiguous()) 

'''
This will return False and if we try to use view now,
This is because in memory it was stored [0, 1, 2, ... 8], whereas now it's [0, 3, 6, 1, 4, 7, 2, 5, 8]
The jump is no longer 1 in memory for one element jump (matrices are stored as a contiguous block, and
using pointers to construct these matrices). This is a bit complicated and I need to explore this more
as well, at least you know it's a problem to be cautious of! A solution is to do the following
'''

print(y_cont.contiguous().view(9))  # Calling .contiguous() before view and it works

# Add two tensors dimensions togethor

x1 = torch.rand(2, 5)
x2 = torch.rand(2, 5)
print(torch.cat((x1, x2), dim=0).shape)  # Shape: 4x5
print(torch.cat((x1, x2), dim=0).shape)

# If we instead have an additional dimension and we wish to keep those as it is we can do:
batch = 64
x = torch.rand((batch, 2, 5))
z_unchanged = x.view(batch,-1)
print(x.unsqueeze(0).shape)
print(z_unchanged.shape)

'''
switch x axis so that instead of 64x2x5 we have 64x5x2
I.e we want dimension 0 to stay, dimension 1 to become dimension 2, dimension 2 to become dimension 1
Basically you tell permute where you want the new dimensions to be, torch.transpose is a special case
'''

z_exchange = x.permute(0, 2, 1)

# Splits x last dimension into chunks of 2 (since 5 is not integer div by 2) the last dimension
# will be smaller, so it will split it into two tensors: 64x2x3 and 64x2x2
z = torch.chunk(x, chunks=2, dim=1)
print(z[0].shape)
print(z[1].shape)

# Let's say we want to add an additional dimension
x_ad_dim = torch.arange((10))  # Shape is [10], let's say we want to add an additional so we have 1x10
print(x_ad_dim.unsqueeze(0).shape)  # 1x10
print(x.unsqueeze(1).shape)  # 10x1
