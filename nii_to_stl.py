from voxelfuse.voxel_model import VoxelModel
from voxelfuse.mesh import Mesh
from voxelfuse.primitives import generateMaterials
import nibabel

#Load nifti mask and convert to numpy
mask_dir = '' #Put the directory of the mask file here
mask_nifti = nibabel.load(mask_dir)
mask_npy = mask_nifti.get_fdata()

#Convert all nonzero labels (i.e. lesion labels) to 1
mask_npy[mask_npy != 0] = 1

#Convert to mesh and save 
model = VoxelModel(mask_npy, generateMaterials(1))
mesh = Mesh.fromVoxelModel(model)
mesh.export('mesh.stl')
