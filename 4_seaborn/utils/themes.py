def set_theme(style='darkgrid', palette='deep', font_scale=1.0):
    import seaborn as sns
    sns.set_theme(style=style, palette=palette, font_scale=font_scale)

def reset_theme():
    import seaborn as sns
    sns.reset_defaults()

def custom_theme():
    import seaborn as sns
    sns.set_theme(style='whitegrid', palette='pastel', font_scale=1.2)
    # Additional customizations can be added here
    # For example, changing the context or modifying specific parameters
    sns.set_context("notebook", font_scale=1.2)