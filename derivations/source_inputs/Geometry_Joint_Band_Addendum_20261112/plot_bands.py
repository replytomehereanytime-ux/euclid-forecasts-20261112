from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
ROOT=Path(__file__).resolve().parent
j=json.loads((ROOT/'RESULT_higher.json').read_text())
c=next(x for x in j['cases'] if (x['prior'],x['model'],x['grid'])==('primary','free_A','primary'))
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'axes.spines.top':False,'axes.spines.right':False})
fig,axes=plt.subplots(1,3,figsize=(12.6,5.3),sharex=True)
for ax,(obs,label) in zip(axes,[('DM_over_rd',r'$D_M/r_d$'),('DH_over_rd',r'$D_H/r_d$'),('F_AP',r'$F_{AP}$')]):
 rows=[r for r in c['bands'] if r['observable']==obs];z=[r['z'] for r in rows];x=list(range(len(z)))
 for k,r in enumerate(rows):
  med=r['median'];joint=[100*(r['joint_lower']/med-1),100*(r['joint_upper']/med-1)];point=[100*(r['original_lower']/med-1),100*(r['original_upper']/med-1)]
  ax.vlines(k,*joint,color='#9cb8dd',linewidth=10,zorder=1)
  ax.hlines(joint,k-.15,k+.15,color='#587bac',linewidth=1.6,zorder=2)
  ax.vlines(k,*point,color='#d67625',linewidth=3.5,zorder=3)
  ax.hlines(point,k-.10,k+.10,color='#a85416',linewidth=1.6,zorder=4)
 ax.axhline(0,color='#263950',linewidth=.9,zorder=5)
 ax.set_xticks(x,[f'{v:g}' for v in z]);ax.set_xlabel('Frozen redshift');ax.set_title(label,pad=10,fontsize=15)
 ax.grid(axis='y',color='#e9edf2',linewidth=.8);ax.set_axisbelow(True);ax.set_xlim(-.4,4.4)
axes[0].set_ylabel('Offset from unchanged median (%)')
fig.suptitle('Pointwise bands and a joint envelope',x=.055,ha='left',y=.98,fontsize=19,fontweight='bold')
fig.text(.055,.91,'Unchanged free-A flat ΛCDM posterior  |  Primary prior  |  Old DESI calibration only',ha='left',fontsize=11,color='#40516a')
handles=[Line2D([0],[0],color='#d67625',lw=4,label='Original pointwise 95% intervals'),Line2D([0],[0],color='#9cb8dd',lw=8,label='New finite-grid joint 95% envelope')]
fig.legend(handles=handles,loc='lower center',bbox_to_anchor=(.5,.115),ncol=2,frameon=False)
fig.text(.055,.075,'Across all 15 coordinates: original joint posterior mass 86.211%; new envelope 95%. Half-widths expand by 23.06%.',fontsize=10,color='#25374c')
fig.text(.055,.035,'Latent posterior uncertainty, not Euclid measurement errors or frequentist coverage. No continuous-redshift claim for this envelope.',fontsize=9.4,color='#576575')
fig.subplots_adjust(left=.085,right=.98,bottom=.27,top=.78,wspace=.28)
fig.savefig(ROOT/'Joint_Latent_Bands_20261112.png',dpi=180,facecolor='white')
fig.savefig(ROOT/'Joint_Latent_Bands_20261112.svg',facecolor='white',metadata={'Date':'2026-11-12','Description':'Finite-grid latent posterior bands. No new observational data.'})
print('Figure generated from retained result rows only.')
