import React, { useEffect, useState } from "react";

import { Bar } from "react-chartjs-2";
import zoomPlugin from "chartjs-plugin-zoom";
import {
  CategoryScale,
  Chart as ChartJS,
  ArcElement,
  Tooltip,
  Legend,
  BarElement,
  Title,
  LinearScale,
  PointElement,
  LineController,
  LineElement,
} from "chart.js";
ChartJS.register(
  PointElement,
  LineController,
  LineElement,
  LinearScale,
  CategoryScale,
  BarElement,
  zoomPlugin
);

const data = {
  labels: ["January", "February", "March", "April", "May", "June"],
  datasets: [
    {
      label: "Bar Dataset",
      data: [10, 20, 30, 40, 50, 60],
      backgroundColor: "rgba(75,192,192,0.4)",
      borderColor: "rgba(75,192,192,1)",
      borderWidth: 1,
      type: "bar",
    },
    {
      label: "Line Dataset",
      data: [60, 50, 40, 30, 20, 10],
      fill: false,
      borderColor: "#742774",
      type: "line",
    },
  ],
};

const options = {
  plugins: {
    zoom: {
      zoom: {
        wheel: {
          enabled: true,
        },
        pinch: {
          enabled: true,
        },
        mode: "xy",
      },
    },
  },
};

export default function Charts() {
  const [chartData, setChartData] = useState();
  const [chartDataOptions, setChartDataOptions] = useState();

  return (
    <div style={{ width: "50%", height: "50%" }}>
      <Bar data={data} options={options} />
    </div>
  );
}
