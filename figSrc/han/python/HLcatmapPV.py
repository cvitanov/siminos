import matplotlib.pyplot as plt
import numpy as np
from scipy import weave
from scipy.weave import converters

lattice = np.zeros([500,1000])
lattice1 = np.zeros([500,1000])
lattice2 = np.zeros([500,1000])
lx = range(500)
ly = range(1000)

a = 1 / (0.5 * (3 + np.sqrt(5)))
b = 1 / (0.5 * (3 - np.sqrt(5)))

for x in lx:
	for y in ly:
		if x>=250 and x<=499 and y>=500 and y<=749:
			lattice[x,y]=-1

#plt.figure(1)
#plt.imshow(lattice.T,origin='lower',cmap='seismic')
#plt.show()

code = """
int Lx1 = 500-1;
int Ly1 = 1000-1;

float aa = a;
float bb = b;

for(int i = 0; i < Lx1; i++){
for(int j = 0; j < Ly1; j++){

float i1 = (i-250)/250.0;
float j1 = (j-500)/250.0;


if(lattice(i,j)!=0){

    if(j1 < (bb * i1 - bb + 1) and i1 < 1 and j1 >= 0){
    lattice(i-250,j) = lattice(i,j);
    lattice(i,j) = 0;
    }
    if(j1 < 1 and j1 >= (aa*i1-aa+1) and i1 >= 0){
    lattice(i,j-250) = lattice(i,j);
    lattice(i,j) = 0;
    }

}


}
}

for(int i = 0; i < Lx1; i++){
for(int j = 0; j < Ly1; j++){

float i1 = (i-250)/250.0;
float j1 = (j-500)/250.0;


if(lattice(i,j)!=0){

    if(j1 < (bb * i1 + 1) and i1 < 0 and j1 >= (aa*i1-aa+1)){
    lattice(i,j-250) = lattice(i,j);
    lattice(i,j) = 0;
    }
    if(j1 < 0 and j1 >= (aa*i1-aa) and j1 < (bb*i1-bb+1)){
    lattice(i-250,j) = lattice(i,j);
    lattice(i,j) = 0;
    }

}


}
}


"""
weave.inline(code, ['a','b','lattice'], type_converters=converters.blitz, compiler='gcc')

code = """
    int Lx1 = 500-1;
    int Ly1 = 1000-1;
    
    float aa = a;
    float bb = b;
    
    for(int i = 0; i < Lx1; i++){
    for(int j = 0; j < Ly1; j++){
    
    float i1 = (i-250)/250.0;
    float j1 = (j-500)/250.0;
    
    
    if(lattice(i,j)!=0){
    
    if(j1 < (aa * i1)){
    lattice(i,j) = -2;
    }
    if(j1 >= (bb * i1)){
    lattice(i,j) = 1;
    }
    
    }
    
    
    }
    }
    """
weave.inline(code, ['a','b','lattice'], type_converters=converters.blitz, compiler='gcc')

plt.figure(1)
plt.imshow(lattice.T,origin='lower',cmap='seismic',vmin=-3.8, vmax=+4)
#plt.axis('off')
ax = plt.gca();
ax.set_xticks(np.arange(0, 500, 250));
ax.set_yticks(np.arange(0, 1000, 250));
ax.set_xticklabels(np.arange(-1,1,1))
ax.set_yticklabels(np.arange(-2,2,1))
ax.grid( linestyle='-', linewidth=2)
plt.savefig('HLcatmapPV1.png')
#plt.show()


code = """
    int Lx1 = 500-1;
    int Ly1 = 1000-1;
    
    for(int i = 0; i < Lx1; i++){
    for(int j = 0; j < Ly1; j++){
    if(lattice(i,j) != 0){
    int x1 = (j-500) + 250;
    int y1 = -1 * (i-250) + 3 * (j-500) + 500;
    x1 = x1 % 500;
    y1 = y1 % 1000;
    if(x1<0){x1=x1+1000;}
    if(y1<0){y1=y1+750;}
    lattice1(x1,y1) = lattice(i,j);
    }
    }
    }
    """
weave.inline(code, ['lattice', 'lattice1'], type_converters=converters.blitz, compiler='gcc')

plt.figure(2)
plt.imshow(lattice1.T,origin='lower',cmap='seismic',vmin=-3.8, vmax=+4)
#plt.axis('off')
#plt.savefig('catmap1.6_figure_2.png')
ax = plt.gca();
ax.set_xticks(np.arange(0, 500, 250));
ax.set_yticks(np.arange(0, 1000, 250));
ax.set_xticklabels(np.arange(-1,1,1))
ax.set_yticklabels(np.arange(-2,2,1))
ax.grid( linestyle='-', linewidth=2)
plt.savefig('HLcatmapPV2.png')
plt.show()

code = """
    int Lx1 = 500-1;
    int Ly1 = 1000-1;
    
    float aa = a;
    float bb = b;
    
    for(int i = 0; i < Lx1; i++){
    for(int j = 0; j < Ly1; j++){
    
    int x1 = i - 250;
    int y1 = j - 500;
    
    if (lattice1(i,j) != 0){
    
    int x2 = x1 % 250;
    if (x2<0) {x2=x2+250;}
    int y2 = y1 % 250;
    if (y2<0) {y2=y2+250;}
    
    int x1d = x1 / 250;
    int y1d = y1 / 250;
    
    if (x1<0) {x1d--;}
    if (y1<0) {y1d--;}
    
    float i1 = x2/250.0;
    float j1 = y2/250.0;
    
    
    lattice2(x2+250,y2+500) = lattice1(i,j) + 2*atan(1) * (x1d + y1d);
    lattice1(i,j) = lattice1(i,j) + 2*atan(1) * (x1d + y1d);
    
    if (i<100){
    lattice2(x2+250,y2+500) = lattice2(x2+250,y2+500)+4*2*atan(1);
    lattice1(i,j) = lattice1(i,j) + 2*atan(1) * 2;
    }
    
    
    if(j1 < (bb * i1 - bb + 1) and i1 < 1 and j1 >= 0){
    lattice2(x2,y2+500) = lattice2(x2+250,y2+500)+2*atan(1);
    lattice2(x2+250,y2+500) = 0;
    lattice1(i,j) = lattice1(i,j)+2*atan(1);
    
        if(j1 >= (aa*(i1-1)-aa+1)) {
        lattice2(x2,y2+250) = lattice2(x2,y2+500)+2*atan(1);
        lattice2(x2,y2+500) = 0;
        lattice1(i,j) = lattice1(i,j)+2*atan(1);
        }
    
    }
    if(j1 < 1 and j1 >= (aa*i1-aa+1) and i1 >= 0){
    lattice2(x2+250,y2+250) = lattice2(x2+250,y2+500)+2*atan(1);
    lattice2(x2+250,y2+500) = 0;
    lattice1(i,j) = lattice1(i,j)+2*atan(1);
    
        if(j1 < (bb*i1-bb+2)) {
        lattice2(x2,y2+250) = lattice2(x2+250,y2+250)+2*atan(1);
        lattice2(x2+250,y2+250) = 0;
        lattice1(i,j) = lattice1(i,j)+2*atan(1);
        }
    
    }

    
    }
    
    }
    }
    """
weave.inline(code, ['a','b','lattice2', 'lattice1'], type_converters=converters.blitz, compiler='gcc')

plt.figure(3)
plt.imshow(lattice1.T,origin='lower',cmap='seismic',vmin=-3.8, vmax=+4)
#plt.axis('off')
#plt.savefig('catmap1.6_figure_3.png')
#plt.colorbar()
#plt.show()
ax = plt.gca();
ax.set_xticks(np.arange(0, 500, 250));
ax.set_yticks(np.arange(0, 1000, 250));
ax.set_xticklabels(np.arange(-1,1,1))
ax.set_yticklabels(np.arange(-2,2,1))
ax.grid( linestyle='-', linewidth=2)
plt.savefig('HLcatmapPV3.png')

plt.figure(4)
plt.imshow(lattice2.T,origin='lower',cmap='seismic',vmin=-3.8, vmax=+4)
#plt.axis('off')
#plt.savefig('catmap1.6_figure_4.png')
ax = plt.gca();
ax.set_xticks(np.arange(0, 500, 250));
ax.set_yticks(np.arange(0, 1000, 250));
ax.set_xticklabels(np.arange(-1,1,1))
ax.set_yticklabels(np.arange(-2,2,1))
ax.grid( linestyle='-', linewidth=2)
plt.savefig('HLcatmapPV4.png')
plt.show()
