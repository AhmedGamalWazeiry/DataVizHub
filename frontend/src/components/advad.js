//https://mui.com/store/previews/minimal-dashboard-free/

import React, { useEffect, useState } from "react";
import { Bar } from "react-chartjs-2";
import zoomPlugin from "chartjs-plugin-zoom";
import Style from "./Charts.module.css";
import { Chart as ChartJS, registerables } from "chart.js";
ChartJS.register(...registerables, zoomPlugin);

const data = {
  labels: [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
  ],
  datasets: [
    {
      label: "Bar Dataset",
      data: [10, 20, 30, 40, 50, 60, 40, 50, 60, 40, 50, 60],
      backgroundColor: "rgba(25,119,242,255)",
      borderColor: "rgba(25,119,242,255)",
      borderRadius: 10,
      borderWidth: 1,
      type: "bar",
    },
    {
      label: "Bar Dataset",
      data: [10, 20, 30, 40, 50, 60, 40, 50, 60, 40, 50, 60],
      backgroundColor: "#ffc143",
      borderColor: "#ffc143",
      borderRadius: 10,
      borderWidth: 1,
      type: "bar",
    },
    {
      label: "Bar Dataset",
      data: [10, 20, 30, 40, 50, 60, 40, 50, 60, 40, 50, -60],
      backgroundColor: "#5fd3e7",
      borderColor: "#5fd3e7",
      borderRadius: 10,
      borderWidth: 1,
      type: "bar",
    },
    {
      label: "Line Dataset",
      data: [10, 20, 30, 40, 50, 60, 40, 50, 60, 40, 50, -60],
      fill: false,
      borderColor: "#5fd3e7",
      borderRadius: 10,
      type: "line",
    },
  ],
};

const options = {
  plugins: {
    zoom: {
      pan: {
        enabled: true,
        mode: "x",
        speed: 0.1,
      },
      zoom: {
        wheel: {
          enabled: true,
          speed: 0.000000001,
        },
        pinch: {
          enabled: true,
        },
        mode: "x",
      },
    },
  },
  scales: {
    x: {
      border: {
        color: "white",
      },
      ticks: {
        color: "#a3aeb9",
        backdropColor: "yallow",
        textStrokeColor: "blue",
      },
      grid: {
        display: false,
        color: "red",
        tickColor: "red",
      },
    },
    y: {
      ticks: {
        color: "#a3aeb9",
        backdropColor: "yallow",
        textStrokeColor: "blue",
      },
      max: 120,
      border: {
        color: "white",
        dash: [4, 4],
      },
      grid: {
        drawTicks: false,
        //display: false,
        color: "rgb(238, 236, 236)", // Set display to false to hide the y-axis grid lines
      },
    },
  },
};

export default function Charts({ revenueList, expensesList, profitList }) {
  return (
    <div
      className={Style["charts__container"]}
      style={{ position: "relative", height: "60vh", width: "60vw" }}
    >
      <Bar data={data} options={options} />
    </div>
  );
}
