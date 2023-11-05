"""Custom faces dataset."""
import os

import torch
from PIL import Image
from torch.utils.data import Dataset


class FacesDataset(Dataset):
    """Faces dataset.

    Attributes:
        root_path: str. Directory path to the dataset. This path has to
        contain a subdirectory of real images called 'real' and a subdirectory
        of not-real images (fake / synthetic images) called 'fake'.
        transform: torch.Transform. Transform or a bunch of transformed to be
        applied on every image.
    """
    def __init__(self, root_path: str, transform=None):
        """Initialize a faces dataset."""
        self.root_path = root_path
        self.real_image_names = os.listdir(os.path.join(self.root_path, 'real'))
        self.fake_image_names = os.listdir(os.path.join(self.root_path, 'fake'))
        self.transform = transform

    def __getitem__(self, index) -> tuple[torch.Tensor, int]:
        """ 0 for real images and 1 for fake/synthetic images. """

        #Label
        fake_count = len(self.fake_image_names) #max index of fake image
        temp = int(index/fake_count)            # temp is 1 if we have real image and 0 if we have fake one
        label = 1 - temp                        # label is 0 if we have real image and 1 if we have fake one

        #Image
        image_path = self.real_image_names
        if label:
            image_path = self.fake_image_names

        image = io.imread(image_path[index])

        item = (image, label)

        return item

        """Get a sample and label from the dataset."""
        """INSERT YOUR CODE HERE, overrun return."""
        #return torch.rand((3, 256, 256)), int(torch.randint(0, 2, size=(1, )))

    def __len__(self):
        """Return the number of images in the dataset."""
        res = len(self.real_image_names)+len(self.fake_image_names)
        """INSERT YOUR CODE HERE, overrun return."""
        return res
