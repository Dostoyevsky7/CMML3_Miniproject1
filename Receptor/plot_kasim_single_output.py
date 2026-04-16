import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

plt.rcParams['pdf.fonttype'] = 42
plt.rcParams['ps.fonttype'] = 42
plt.rcParams['font.family'] = 'Arial'
plt.rcParams['font.size'] = 10

# =========================================================
# 在这里改文件名
# =========================================================
input_file = "output_sTheta_60.out"   # 改成 output_HFS.out
label = "sTheta60"                 # 改成 HFS

# 是否只看前多少秒；None 表示全程
time_max = None
# 例如想只看前10秒：time_max = 10
# =========================================================

def read_kasim_out(path):
    # 跳过前两行注释，第三行才是真正表头
    df = pd.read_csv(path, skiprows=2)

    # 去掉列名两侧引号
    df.columns = [str(c).strip().strip('"') for c in df.columns]

    # 统一时间列名
    if "[T]" in df.columns:
        df = df.rename(columns={"[T]": "T"})
    elif "T" not in df.columns:
        raise ValueError(f"找不到时间列 T，当前列为: {df.columns.tolist()}")

    return df

input_vars = [
    "Calcium_Levels",
    "Glutamate_level",
    "CaGlu",
    "Glu_Trigger",
]

mechanism_vars = [
    "Active_CaM",
    "PP2B",
    "cAMP_levels",
    "PKA_a",
    "Phos_CK_subunits",
    "CaMKII_CaM",
    "actPKC_level",
]

phenotype_vars = [
    "Synaptic_receptors",
    "AMPA_membrane",
    "AMPA_PSD",
    "Conductance_S845_measure",
    "Conductance_S831_measure",
    "S845_P",
    "S845_PP",
    "S831_P",
    "S831_PP",
]

def filter_vars(df, vars_list):
    keep = []
    for v in vars_list:
        if v in df.columns:
            keep.append(v)
        else:
            print(f"[跳过] {v} 不存在")
    return keep

def plot_group(df, vars_list, title, outfile):
    vars_list = filter_vars(df, vars_list)
    if len(vars_list) == 0:
        print(f"{title} 没有可画变量")
        return

    n = len(vars_list)
    ncols = 2
    nrows = (n + ncols - 1) // ncols

    fig, axes = plt.subplots(nrows, ncols, figsize=(6*ncols, 3.8*nrows))
    axes = axes.flatten()

    for i, var in enumerate(vars_list):
        ax = axes[i]
        ax.plot(df["T"], df[var])
        ax.set_title(var)
        ax.set_xlabel("Time")
        ax.set_ylabel("Level")
        ax.grid(True, alpha=0.3)

    for j in range(i + 1, len(axes)):
        axes[j].axis("off")

    fig.suptitle(title)
    fig.tight_layout(rect=[0, 0, 1, 0.96])
    fig.savefig(outfile, dpi=300)
    plt.close()
    print(f"Saved: {outfile}")

def plot_overlay(df, vars_list, title, outfile):
    vars_list = filter_vars(df, vars_list)
    if len(vars_list) == 0:
        return

    plt.figure(figsize=(10, 6))

    for var in vars_list:
        max_val = df[var].max()
        if max_val == 0:
            continue
        plt.plot(df["T"], df[var] / max_val, label=var)

    plt.title(title + " (normalized)")
    plt.xlabel("Time")
    plt.ylabel("Normalized level")
    plt.legend(fontsize=8, ncol=2)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(outfile, dpi=300)
    plt.close()
    print(f"Saved: {outfile}")

# =========================
# 主程序
# =========================
df = read_kasim_out(input_file)

if time_max is not None:
    df = df[df["T"] <= time_max].copy()

print("检测到列：")
print(df.columns.tolist())

out_dir = Path(f"plots_{label}")
out_dir.mkdir(exist_ok=True)

plot_group(
    df, input_vars,
    f"A. Input layer ({label})",
    out_dir / f"A_input_{label}.pdf"
)

plot_group(
    df, mechanism_vars,
    f"B. Mechanism layer ({label})",
    out_dir / f"B_mechanism_{label}.pdf"
)

plot_group(
    df, phenotype_vars,
    f"C. Output phenotype ({label})",
    out_dir / f"C_output_{label}.pdf"
)

plot_overlay(
    df, input_vars,
    f"A. Input ({label})",
    out_dir / f"A_overlay_{label}.pdf"
)

plot_overlay(
    df, mechanism_vars,
    f"B. Mechanism ({label})",
    out_dir / f"B_overlay_{label}.pdf"
)

plot_overlay(
    df, phenotype_vars,
    f"C. Output ({label})",
    out_dir / f"C_overlay_{label}.pdf"
)

print("\n全部完成")