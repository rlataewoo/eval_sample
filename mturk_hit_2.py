
def generate_classifier_block(sample_num, transcript):
    sample_id = f"sample_{sample_num:03d}"
    audio_url = f"https://rlataewoo.github.io/eval_sample/samples/table_1/libritts_mp3/{sample_id}.mp3?raw=true"
    
    return f"""
    <crowd-classifier 
        categories="['Excellent - Completely natural speech - 5', '4.5', 'Good - Mostly natural speech - 4', '3.5', 'Fair - Equally natural and unnatural speech - 3', '2.5', 'Poor - Mostly unnatural speech - 2', '1.5', 'Bad - Completely unnatural speech - 1']"
        header="How natural does the edited segment of the speech sound? Please focus on whether the transition between the original and synthesized parts is smooth and human-like."
        name="{sample_id}-naturalness">
            <classification-target>
                <audio controls style="width: 100%">
                    <source src="{audio_url}" type="audio/mp3" />
                </audio>
                <div class="sample-number" style="margin-top: 10px; margin-bottom: 10px; font-weight: bold; font-size: 30px;">Sample {sample_num:03d}</div>
                <div id="text_area">
                    <h3>Transcripts (edited parts are shown in <span style='color: red;'>red</span>)</h3>
                    <p>{transcript}</p>
                </div>
            </classification-target>
        <short-instructions>  
            <p>
              Listen to the sample of computer generated speech and assess the quality 
              of the audio based on how close it is to natural speech. The words in the audio are shown in the Original utterance below.
            </p>
            For better results, wear headphones and work in a quiet environment.
            If the audio file is not playing, please be patient as it may take some time for the audio file to upload.
        </short-instructions>
    </crowd-classifier>
    """

def generate_hit_file(filename, start_idx, end_idx, transcript_map):
    html_blocks = ['<!-- You must include this JavaScript file -->',
                   '<script src="https://assets.crowd.aws/crowd-html-elements.js"></script>',
                   '<crowd-form answer-format="flatten-objects">']
    
    for i in range(start_idx, end_idx + 1):
        transcript = next(val for key, val in transcript_map.items() if i in key)
        html_blocks.append(generate_classifier_block(i, transcript))

    html_blocks.append('</crowd-form>')

    full_html = '\n'.join(html_blocks)

    with open(filename, "w", encoding="utf-8") as f:
        f.write(full_html)


# 각 샘플 번호와 대응하는 텍스트
transcript_map = {
    range(1, 7+1): "You see loving <span style='color: red;'>some one as I love you</span> makes the whole world different.",
    range(8, 14+1): "At any rate my <span style='color: red;'>eloquence was altogether stopped. The gentleman</span> was named Sir Ferdinando Brown.",
    range(15, 21+1): "Mary your father and I are going out <span style='color: red;'>to ride this afternoon and I am sorry for your</span> sake that we can not take you with us.",
    range(22, 28+1): "Whoever therefore is ambitious <span style='color: red;'>of distinction in this way ought</span> to be prepared for disappointment.",
    range(29, 35+1): "I wonder though if people <span style='color: red;'>could see the light from the street</span> through any chinks in the boarding?",
    range(36, 42+1): "The Abraham Lincoln <span style='color: red;'>had been perfectly chosen and fitted</span> out for its new assignment.",
    range(43, 49+1): "Ten days were consumed <span style='color: red;'>in these negotiations; but the spirit</span> of vengeance refused to yield.",
    range(50, 56+1): "The wheat cutting sometimes goes on all night <span style='color: red;'>as well as all day and in good seasons there</span> are scarcely men and horses enough to do the harvesting.",
    range(57, 63+1): "I have very few to love <span style='color: red;'>me now and I thought you might love</span> me as I have begun to love you.",
    range(64, 70+1): "My dear Sir I <span style='color: red;'>should reply (or Madam) you have</span> come to the right shop.",

    range(71, 77+1): "'We indeed!' cried the <span style='color: red;'>Mouse who was trembling down to</span> the end of his tail.",
    range(78, 84+1): "Surely some portion <span style='color: red;'>of the Casbah must still</span> rise above the waves?",
    range(85, 91+1): "As for ourselves we shall soon <span style='color: red;'>reach some retired spot where no eyes can</span> see us and no step follow ours.",
    range(92, 98+1): "The first person he met <span style='color: red;'>was a farm labourer walking alongside a load</span> of peat and smacking at his horse.",
    range(99, 105+1): "That is <span style='color: red;'>all quite true Mr Neverbend</span> said Sir Ferdinando Brown.",
    range(106, 112+1): "The first page on the <span style='color: red;'>floor the second in the window the</span> third where you left it said he.",
    range(113, 119+1): "As they led the <span style='color: red;'>now famous animal from the room</span> the Boolooroo shuddered and said:",
    range(120, 126+1): "I remained there alone for many hours but I <span style='color: red;'>must acknowledge that before I left the chambers I had gradually</span> brought myself to look at the matter in another light.",
    range(127, 133+1): "The etiquette is to have <span style='color: red;'>two bites before the butler and the</span> three footmen whisk away the plate.",
    range(134, 140+1): "But the affair was magnified <span style='color: red;'>as a crowning proof that the free</span> State men were insurrectionists and outlaws.",

    range(141, 147+1): "But it is not with a <span style='color: red;'>view to distinction that you should cultivate this</span> talent if you consult your own happiness.",
    range(148, 154+1): "First bind the Earth Man in the <span style='color: red;'>frame commanded the Boolooroo. We'll slice him in two</span> before we do the same to the billygoat.",
    range(155, 161+1): "Can you give me a few <span style='color: red;'>hints? --suppose you spoke to me like this</span> then I could do something for you.",
    range(162, 168+1): "During and after the contest <span style='color: red;'>over the speakership at Washington each State</span> Legislature became a forum of Kansas debate.",
    range(169, 175+1): "This trading votes <span style='color: red;'>which was often done was considered</span> by the politicians quite legitimate.",
    range(176, 182+1): "Sheriff Jones made several visits unmolested on <span style='color: red;'>their part and without any display of writs or demand</span> for the surrender of alleged offenders on his own.",
    range(183, 189+1): "It seems to <span style='color: red;'>be easier than it is I</span> begin to think replied Philip.",
    range(190, 196+1): "All were agreed that one could be <span style='color: red;'>ordered but that it was not a usual size of</span> pencil and that it was seldom kept in stock.",
    range(197, 203+1): "Hold him steady <span style='color: red;'>in the frame and I'll</span> tie him up she replied.",
    range(204, 210+1): "Oh she said he has such <span style='color: red;'>an extraordinarily fine cap on his head that that</span> will do just as well as a uniform.",

    range(211, 217+1): "Yes indeed those are the marks <span style='color: red;'>of teeth imprinted upon the metal! The jaws which</span> they arm must be possessed of amazing strength.",
    range(218, 224+1): "It went into service <span style='color: red;'>august fifteenth eighteen eighty two about three</span> weeks before the Pearl Street station.",
    range(225, 231+1): "The master and mistress begged them not <span style='color: red;'>to cry or raise their voices in lamentation; for</span> it would do the little patient no good.",
    range(232, 238+1): "Yes yes she hurried pulling <span style='color: red;'>her hand gently away from him. Presently</span> it stole back to his coat sleeve.",
    range(239, 245+1): "I want to be <span style='color: red;'>something to make myself something</span> to do something.",
    range(246, 252+1): "Then dear said mrs Whitney you must be kinder <span style='color: red;'>to her than ever; think what it would be for one</span> of you to be away from home even among friends.",
    range(253, 259+1): "One day when the boy was sent by his <span style='color: red;'>grandfather with a message to a relation he passed along a</span> street in which there was a great concourse of horsemen.",
    range(260, 266+1): "I had however promised to <span style='color: red;'>take tea in a friend's rooms so</span> I left the proof upon my desk.",
    range(267, 273+1): "Fairview was twelve miles <span style='color: red;'>away but by ten o'clock they</span> drew up at the county jail.",
    range(274, 280+1): "Don't mind him <span style='color: red;'>Cap'n said Trot but fetch</span> him along to the frame.",


}

generate_hit_file("hit_1_libritts.html", 1, 70, transcript_map)
generate_hit_file("hit_2_libritts.html", 71, 140, transcript_map)
generate_hit_file("hit_3_libritts.html", 141, 210, transcript_map)
generate_hit_file("hit_4_libritts.html", 211, 280, transcript_map)
