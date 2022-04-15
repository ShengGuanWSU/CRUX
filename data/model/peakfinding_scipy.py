import xmltodict
import numpy as np
from scipy.signal import find_peaks


def peak_finding(input, output):
    """
    :param input: Path to XRDML file.
    :param output: Path to the output txt file.
    :return: Peaklist with positions and intensities
    """
    f = open(input, mode='r', encoding='utf-8')
    dic = xmltodict.parse(f.read())

    dp = dic["xrdMeasurements"]["xrdMeasurement"]["scan"]["dataPoints"]
    y = dp["intensities"]["#text"]
    y = list(map(int, y.split()))
    sp = float(dp["positions"][0]["startPosition"])
    ep = float(dp["positions"][0]["endPosition"])
    x = np.arange(sp, ep, (ep - sp) / len(y))
    peaks, _ = find_peaks(y)
    peak_position = []
    peak_intensity = []
    f = open(output, 'w')
    f.write('pos' + '\t' + 'int' + '\t' + '\n')

    for peak in peaks:
        position = format(x[peak], '.4f')
        intensity = format(y[peak], '.2f')
        peak_position.append(position)
        peak_intensity.append(intensity)
        f.write(str(position) + '\t' + str(intensity) + '\t' + '\n')
    f.close()

    return peak_position, peak_intensity


def main():
    input = "../../data/test/MnO2_Unmilled_Air_InitialScan.xrdml"
    output = "../../data/test/pk_scipy.txt"

    peak_finding(input, output)


if __name__ == "__main__":
    main()
