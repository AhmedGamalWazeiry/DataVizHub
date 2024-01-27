import React, { useState } from "react";
import Charts from "./Charts";
import Form from "./Form";
import { data } from "./utils";
import Style from "./AnalyticsDashboard.module.css";
import FileTap from "./FileTab";
import Tap from "./Tab";

export default function AnalyticsDashboard() {
  const [chartData, setChartData] = useState(data);

  return (
    <div className={Style["dashboard"]}>
      <Charts chartData={chartData} />

      <div className={Style["dashboard__form"]}>
        <Form setChartData={setChartData} />
        <Tap setChartData={setChartData} chartData={chartData} />
      </div>
    </div>
  );
}
