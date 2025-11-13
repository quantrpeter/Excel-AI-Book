import tensorflow as tf

# create 3d tensor
tensor_3d = tf.constant([[[1, 2, 3],
						  [4, 5, 6]],
						 [[7, 8, 9],
						  [10, 11, 12]]])

# rotate tensor 90 degrees counter-clockwise
print(tensor_3d)
rotated_tensor = tf.image.rot90(tensor_3d)
print(rotated_tensor)