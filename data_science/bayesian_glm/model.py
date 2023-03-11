import pymc as pm
import arviz as az
import xarray as xr
import matplotlib.pyplot as plt

def define_model(x, y):
    with pm.Model() as model:
        # Define priors
        sigma = pm.HalfCauchy("sigma", beta=10)
        intercept = pm.Normal("intercept", 0, sigma=20)
        slope = pm.Normal("slope", 0, sigma=20)

        # Define likelihood
        likelihood = pm.Normal("y", mu=intercept + slope * x, sigma=sigma, observed=y)

    return model


def inference(model, sample_size=3000):
    with model:
        idata = pm.sample(sample_size)
    return model, idata


if __name__ == "__main__":
    from data_generation import sample_xy

    x, y, line = sample_xy(intercept_gen=3, slope_gen=2)
    model = define_model(x, y)
    model, idata = inference(model)

    # TODO: Analysis for glm result
    idata.posterior["y_model"] = idata.posterior["intercept"] + idata.posterior["slope"] * xr.DataArray(x)
    fig, ax = plt.subplots(figsize=(7, 7))
    ax.set_title("Posterior predictive regression lines")
    az.plot_lm(idata=idata, y="y", num_samples=100, axes=ax, y_model="y_model")
    ax.set_xlabel("x")
    plt.show()
