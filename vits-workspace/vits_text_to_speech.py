import argparse
from modules import utils
from modules import commons
import torch
from modules.models import SynthesizerTrn
from modules.text import text_to_sequence
from torch import no_grad, LongTensor
import wave
from scipy.io.wavfile import write


def get_text(text, hps):
    text_norm= text_to_sequence(text, hps.data.text_cleaners)
    if hps.data.add_blank:
        text_norm = commons.intersperse(text_norm, 0)
    text_norm = LongTensor(text_norm)
    return text_norm

def create_tts_fn(net_g_ms):
    def tts_fn(text, noise_scale, noise_scale_w, length_scale, speaker_id):
        text = text.replace('\n', ' ').replace('\r', '').replace(" ", "")
        stn_tst= get_text(text, hps_ms)
        with no_grad():
            x_tst = stn_tst.unsqueeze(0).to(device)
            x_tst_lengths = LongTensor([stn_tst.size(0)]).to(device)
            sid = LongTensor([speaker_id]).to(device)
            audio = net_g_ms.infer(x_tst, x_tst_lengths, sid=sid, noise_scale=noise_scale, noise_scale_w=noise_scale_w,
                                   length_scale=length_scale)[0][0, 0].data.cpu().float().numpy()
        return audio
    return tts_fn

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--device', type=str, default='cpu')
    parser.add_argument('-c', '--config', type=str, default="configs/config-jvs.json", help='JSON file for configuration')
    parser.add_argument('-m', '--model', type=str, required=False, default="./models/jvs_model/G_212000.pth", help='Model path')
    args = parser.parse_args()
    
    device = torch.device(args.device)
    hps_ms = utils.get_hparams_from_file(args.config)
    net_g_ms = SynthesizerTrn(
        len(hps_ms.symbols),
        hps_ms.data.filter_length // 2 + 1,
        hps_ms.train.segment_size // hps_ms.data.hop_length,
        n_speakers=hps_ms.data.n_speakers,
        **hps_ms.model)
    utils.load_checkpoint(args.model, net_g_ms, None)
    net_g_ms = net_g_ms.eval().to(device)

    tts_fn = create_tts_fn(net_g_ms)
    text = input("Enter text: ")
    audio = tts_fn(text, noise_scale=0, noise_scale_w=0, length_scale=1.0, speaker_id=0)
    write("jvs.wav",22050,audio)
