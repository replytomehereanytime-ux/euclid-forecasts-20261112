cd /workspace/r03-out/euclid_forecast_bot/R02
{ find . -type f ! -name SHA256SUMS ! -name '*.bak_pre_cov' ! -path '*/__pycache__/*' | sort | xargs sha256sum
  cd /workspace/r03-out; sha256sum euclid_forecast_bot/FORECASTS_R01.md euclid_forecast_bot/FORECAST_TABLE_R01.csv euclid_forecast_bot/POSTING_ABSTRACT_R01.md euclid_forecast_bot/ZENODO_METADATA_DRAFT_R01.json euclid_forecast_bot/WOLFRAM_CHECKS_R01.md euclid_forecast_bot/SHA256SUMS euclid_20261112/HANDOFF_8925124.md euclid_20261112/HANDOFF_8925124_INVENTORY.md euclid_20261112/wolfram_R04/WOLFRAM_RESULTS_R04.md euclid_20261112/xact_R05/RESULTS_R05.md euclid_20261112/xact_R05/SHA256SUMS | sed 's#  #  ../../#'
  sha256sum /workspace/desi_r01/DESI_PREDICTIONS_source.md; } > /workspace/r03-out/euclid_forecast_bot/R02/SHA256SUMS
